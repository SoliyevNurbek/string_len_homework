def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    if (len(s1)+len(s2)+len(s3))%2==1 :
        return "[s1,s2]"
    else :
        return "[]"
print(main("Nurbek","Doniyor","Ozodbek"))