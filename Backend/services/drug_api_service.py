import requests

def get_drug_info(drug_name):
    """
    Fetch drug details using the OpenFDA API.
    """
    try:
        url = f"https://api.fda.gov/drug/label.json?search=openfda.generic_name:{drug_name}&limit=1"
        response = requests.get(url)
        data = response.json()

        if "results" not in data:
            return {"error": "No information found for this drug."}

        result = data["results"][0]
        info = {
            "brand_name": result["openfda"].get("brand_name", ["Unknown"])[0],
            "purpose": result.get("purpose", ["Not specified"])[0],
            "warnings": result.get("warnings", ["No warnings available"])[0],
        }
        return info

    except Exception as e:
        return {"error": str(e)}
