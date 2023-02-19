import gematria as gem
import random

class MonoCipher:
    """

    """

    def __init__(self):
        self.mono_mapping()

    def mono_mapping(self):
        """ substitution cipher mapping """
        #random.seed(347)
        shuffled_runes = random.sample(gem.runes, len(gem.runes))
        self.encoder_cipher_mapping = {
            gem.runes[i]: shuffled_runes[i] for i in range(len(shuffled_runes))
        }

    def encode(self, message):
        """ encode message with encoder_cipher_mapping """
        message_items  = list(message)
        for i in range(len(message)):
            if message_items[i] in self.encoder_cipher_mapping:
                message_items[i] = self.encoder_cipher_mapping[message_items[i]]
        encoded_message = "".join(message_items)
        return encoded_message

    def decode(self, encoded_message, solution):
        """ method to decode the message using the cipher mapping """
        message_items = list(encoded_message.lower())
        for i in range(len(encoded_message)):
            if message_items[i] in solution:
                message_items[i] = solution[message_items[i]]

        decoded_message = "".join(message_items)
        return decoded_message
