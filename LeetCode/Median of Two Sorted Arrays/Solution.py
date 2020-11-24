class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # 문제에서 시간복잡도를 O(log(m+n))으로 제한했기때문에 두 list를 더한 후 sort를 쓰지못하므로 작은수부터 카운트해서 중간지점을  
        
        m=len(nums1)
        n=len(nums2)
        l=(m+n)%2
        half=(m+n-l)//2
        num=0
        a=0
        b=0
        x=0
        y=0
        while True:
            if a==m or b==n:
                if a==m:
                    x,y=y,nums2[b]
                    b+=1
                else:
                    x,y=y,nums1[a]
                    a+=1
            else:
                if nums1[a]<=nums2[b]:
                    x,y= y, nums1[a]
                    a+=1

                else:
                    x,y=y,nums2[b]
                    b+=1

            if half==num:
                break
            num+=1
        if l:
            return y
        else:
            return (x+y)/2
