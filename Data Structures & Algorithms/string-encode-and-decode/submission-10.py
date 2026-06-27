class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            return "و".join(strs)
        return "no"

    def decode(self, s: str) -> List[str]:
        if s == "no":
            return []
        elif s:
            return s.split("و")
        return [s]