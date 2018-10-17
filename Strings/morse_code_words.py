class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result_set = set()
        for word in words:
            morse_word = ""
            for letter in word:
                morse_word += morse_code[ord(letter) - ord('a')]
            result_set.add(morse_word)
        return len(result_set)