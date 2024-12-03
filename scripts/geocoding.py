import requests
import os
import csv
from urllib.parse import unquote

_ENV_GOOGLE_API_KEY = "GOOGLE_API_KEY"


def get_geocoding_result(address, country_code, api_key=None):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "language": "en",
        "region": country_code.lower(),
        "components": f"country:{country_code}",
        "key": api_key or os.getenv(_ENV_GOOGLE_API_KEY)
    }
    r = requests.get(base_url, params=params)
    r.raise_for_status()
    r = r.json()
    if r["status"] != "OK":
        raise ValueError(f"status = {r['status']}")
    return r["results"][0]


def process_csv(input_csv, key_col, cc_col, addr_col, addr_col2, output_csv):
    with open(output_csv, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["code", "formatted_address", "lat", "lng", "place_id"])
        writer.writeheader()

        # open input csv file
        with open(input_csv) as input_f:
            reader = csv.DictReader(input_f)
            rows = list(reader)
            for row in rows:
                key, cc, addr = row[key_col], row[cc_col], row[addr_col]
                cc = cc.strip()[:2]
                addr = unquote(addr.strip())
                print(f"Processing {key}...")
                result = None
                try:
                    result = get_geocoding_result(addr, cc)
                except Exception as e:
                    print(f"Error processing {key}: {e}")
                    if addr_col2:
                        addr2 = row[addr_col2]
                        addr2 = unquote(addr2.strip())
                        print(f"Trying {addr2}...")
                        try:
                            result = get_geocoding_result(addr2, cc)
                        except Exception as e:
                            print(f"Error processing {key}: {e}")
                writer.writerow({
                    "code": key,
                    "formatted_address": result["formatted_address"] if result else "",
                    "lat": result["geometry"]["location"]["lat"] if result else 0,
                    "lng": result["geometry"]["location"]["lng"] if result else 0,
                    "place_id": result["place_id"] if result else ""
                })


if __name__ == '__main__':
    process_csv("../iso3166-1.csv", "alpha-2", "alpha-2", "name", None, "../iso3166-1-geocoding.csv")
    process_csv("../iso3166-2.csv", "code", "code", "name", "wikipedia", "../iso3166-2-geocoding.csv")
    print("Done.")

