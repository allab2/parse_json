# Word frequency counter with error handling

filename = "words.txt"   # file to read

try:
    # Step 1: Open and read file
    with open(filename, "r") as f:
        text = f.read()

    # Check if file is empty
    if not text.strip():
        print("⚠️ The file is empty.")
        exit()

    # Step 2: Split text into words
    words = text.split()

    # Step 3: Count word frequency
    freq = {}
    for word in words:
        word = word.lower()  # make lowercase so Hello = hello
        freq[word] = freq.get(word, 0) + 1

    # Step 4: Print results
    print("\n--- Word Frequency ---")

    for item in freq:
        print(item, ":", freq[item])

    print(freq)

except FileNotFoundError:
    print(f"❌ Error: File '{filename}' not found.")
except Exception as e:
    print("❌ Unexpected error:", e)
