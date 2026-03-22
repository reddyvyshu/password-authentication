def spam_classifier_ideas():
    system = {
        "Features": [
            "Email text content",
            "Presence of keywords like free, win, offer",
            "Sender email address",
            "Number of links",
            "Use of special characters"
        ],
        "Data Needed": [
            "Collection of spam emails",
            "Collection of non-spam emails",
            "Labeled dataset (spam or not spam)"
        ],
        "Possible Mistakes": [
            "Marking important emails as spam",
            "Missing actual spam emails",
            "Bias due to limited dataset"
        ]
    }

    for key, values in system.items():
        print(key + ":")
        for v in values:
            print("-", v)
        print()

spam_classifier_ideas()
