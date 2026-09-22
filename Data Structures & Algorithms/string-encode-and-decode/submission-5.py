class Solution:

    def encode(self, strs: List[str]) -> str:
        if(len(strs)<=0):
            return ""
        encoded_str = ""
        for s_str in strs:
            encoded_str = encoded_str +  "kathir" + s_str
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = s.split("kathir")
        return decoded_str[1:]
