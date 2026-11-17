import re,sys
p=sys.argv[1]; s=open(p).read()
body,refs=s.split("## References\n",1)
pat=re.compile(r'\[(\d+(?:[–,]\d+)*)\]')
def expand(g):
    out=[]
    for part in g.split(','):
        if '–' in part:
            a,b=map(int,part.split('–')); out+=range(a,b+1)
        else: out.append(int(part))
    return out
order=[]
for m in pat.finditer(body):
    for n in expand(m.group(1)):
        if n not in order: order.append(n)
mp={old:i+1 for i,old in enumerate(order)}
print(mp)
def comp(nums):
    nums=sorted(set(nums)); res=[]; i=0
    while i<len(nums):
        j=i
        while j+1<len(nums) and nums[j+1]==nums[j]+1: j+=1
        res.append(f"{nums[i]}–{nums[j]}" if j-i>=2 else (",".join(map(str,nums[i:j+1]))))
        i=j+1
    return ",".join(res)
body=pat.sub(lambda m:"["+comp([mp[n] for n in expand(m.group(1))])+"]",body)
lines=[l for l in refs.strip().split("\n") if re.match(r'\d+\. ',l)]
d={int(l.split('.')[0]):l.split('. ',1)[1] for l in lines}
assert set(d)==set(mp), (set(d)-set(mp), set(mp)-set(d))
new="\n".join(f"{mp[o]}. {d[o]}" for o in sorted(d,key=lambda o:mp[o]))
open(p,'w').write(body+"## References\n\n"+new+"\n")
