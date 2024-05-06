"""
    Banners down here (^-^' )
"""

class Banner:
    
    def __init__(self, givenip, givenport):
        self.givenip = givenip
        self.givenport = givenport

    def bannerWithArgsServer():
        print("""
        ********** The CHATLY -reborn V1.0.0 cli App **********
                                -- developed by: Ebae-b
              - Don't like leaving the terminal like me? Gotcha!
        [*] Run the Server side of the program
        [*] Type 'quit' to leave the chat.
    -Enjoy (^-^' )...
""")
    
    def bannerWithArgsClient():
         print("""
        ********** The CHATLY -reborn -reborn V1.0.0 cli App **********
                                -- developed by: Ebae-b
              - Don't like leaving the terminal like me? Gotcha!
        [*] Run the Client side of the program
        [*] Type 'quit' to leave the chat.
    -Enjoy (^-^' )...
""")

    def bannerWithoutArgsServer():
        print("""
        ********** The CHATLY -reborn -reborn V1.0.0 cli App **********
                                -- developed by: Ebae-b
              - Don't like leaving the terminal like me? Gotcha!
        [*] Run the Server side of the program
        [*] Type 'quit' to leave the chat.\n
""")
        givenip = input("-Enter your IP address: ")
        givenport = int(input("-Enter a port number, (choose wisely): "))

        print("-Enjoy (^-^' )...")

        return (givenip, givenport)
    
    
    def bannerWithoutArgsClient():
        print("""
        ********** The CHATLY -reborn V1.0.0 cli App **********
                                -- developed by: Ebae-b
              - Don't like leaving the terminal like me? Gotcha!
        [*] Run the Client side of the program
        [*] Type 'quit' to leave the chat.\n
""")
        givenip = input("-Enter the server IP address: ")
        givenport = int(input("-Enter the expected port number, (must be known): "))

        print("-Enjoy (^-^' )...")

        return (givenip, givenport)
        