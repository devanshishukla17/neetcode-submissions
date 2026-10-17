class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n=len(words)
        ans=[]
        line,length=[],0
        i=0
        while i<n:
            if length+len(words[i])+len(line)<=maxWidth:
                line.append(words[i])
                length+=len(words[i])
                i+=1
            else:
                extra=maxWidth-length
                rem= extra% max(1,(len(line)-1))
                space=extra//max(1,(len(line)-1))
                for j in range(max(1,len(line)-1)):
                    line[j]+= " "*space
                    if rem:
                        line[j]+=" "
                        rem-=1
                ans.append("".join(line))
                line,length=[],0
        last=" ".join(line)
        trail=maxWidth-len(last)
        ans.append(last+" "*trail)
        return ans