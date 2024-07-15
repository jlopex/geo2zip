import argparse
from geo_zip import GeoZip

def main():
    parser = argparse.ArgumentParser(description="Find the closest ZIP code for given latitude and longitude.")
    parser.add_argument("latitude", type=float, help="Latitude of the location")
    parser.add_argument("longitude", type=float, help="Longitude of the location")
    args = parser.parse_args()

    geo_zip = GeoZip()
    closest_zip = geo_zip.find_closest_zip(args.latitude, args.longitude)
    print(f"The closest ZIP code to ({args.latitude}, {args.longitude}) is {closest_zip}")

if __name__ == "__main__":
    main()
