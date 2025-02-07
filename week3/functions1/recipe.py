def grams_to_ounces(grams):
    ounces=28.3495231 * grams
    return ounces


if __name__ == "__main__":
    grams=int(input())
    print(grams_to_ounces(grams))