
# ==========================================
# (7,4) Hamming Code Implementation in Python
# ==========================================

# Step 1: Enter the data to be transmitted
data = input("Enter 4-bit binary data: ")

# Check whether the input is valid
if len(data) != 4 or any(bit not in "01" for bit in data):
    print("Error: Please enter exactly 4 binary bits.")

else:
    # Step 2: Calculate the number of redundant bits
    m = len(data)
    r = 0

    while 2 ** r < m + r + 1:
        r += 1

    print("\nNumber of redundant bits:", r)

    # Step 3: Determine the parity bits
    d1, d2, d3, d4 = map(int, data)

    # Even parity using XOR
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p4 = d2 ^ d3 ^ d4

    # Positions: P1 P2 D1 P4 D2 D3 D4
    hamming = [p1, p2, d1, p4, d2, d3, d4]

    print("Original data:", data)
    print("Hamming code:", "".join(map(str, hamming)))

    # Step 4: Create error data for testing
    received = hamming.copy()

    while True:
        try:
            position = int(input(
                "\nEnter error position (1-7, 0 for no error): "
            ))

            if 0 <= position <= 7:
                break
            else:
                print("Please enter a number from 0 to 7.")

        except ValueError:
            print("Please enter a valid number.")

    if position != 0:
        received[position - 1] ^= 1

    print("Received data:", "".join(map(str, received)))

    # Step 5: Check for errors
    s1 = received[0] ^ received[2] ^ received[4] ^ received[6]
    s2 = received[1] ^ received[2] ^ received[5] ^ received[6]
    s4 = received[3] ^ received[4] ^ received[5] ^ received[6]

    # Calculate the error position (syndrome)
    error_position = s1 + 2 * s2 + 4 * s4

    if error_position == 0:
        print("\nNo error detected.")

    else:
        print("\nError detected at position:", error_position)

        # Correct the error
        received[error_position - 1] ^= 1

        print("Error corrected successfully!")

    # Display the corrected Hamming code
    corrected = "".join(map(str, received))
    print("Corrected Hamming code:", corrected)

    # Extract the original 4 data bits
    original = [
        received[2],
        received[4],
        received[5],
        received[6]
    ]

    print("Recovered original data:", "".join(map(str, original)))

    print("\nProgram finished.")
