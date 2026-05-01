def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    ans = []
    for token in tokens:
        if token not in stopwords:
            ans.append(token)

    return ans
            