class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        for i in range(n+1):
            st = f'{i:b}'
            st = st.zfill(n)
            if st not in nums:
                return st
