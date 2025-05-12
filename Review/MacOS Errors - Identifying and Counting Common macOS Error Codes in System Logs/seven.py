from collections import Counter

def get_data():
    code_descriptions = {
        -67062: "Code object is not signed at all", # from Apple Community
        113: "kCFSOCKS4ErrorUnknownStatusCode – server returned an unknown status code",
        22: "EINVAL – Invalid argument",
    }
    counts = Counter({22: 8, -67062: 2, 113: 2})
    data = []
    for code, count in counts.items():
        desc = code_descriptions.get(code, "Unknown")
        data.append({"Error Code": code, "Description": desc, "Occurrences": count})
    return data


if __name__ == "__main__":
    data = get_data()
    print(data)
