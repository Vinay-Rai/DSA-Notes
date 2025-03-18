def checksorted(l1):
    if len(l1)==0 or len(l1)==1:
        return True
    
    ans  = checksorted(l1[1:])

    if l1[0]<l1[1]:
        return ans 
    else:
        return False
    
#YE BETTER WAY HAI BECAUSE ISME CHECK HO RAHA HAI CONDITION FIR RECURSICVE CALL HO RAHA HAI UPAR WALE ME SARE RECURSION CALL HONE KE BAD CONDITION CHECK HONA START HOTI HAI
def checksorted2(l1):
    if len(l1)==0 or len(l1)==1:
        return True
    
    if l1[0]<l1[1]:
        return checksorted2(l1[1:]) 
    else:
        return False
    
# YE WALA BICH WALE JAISA HI HAI
def checksorted2(l1):
    if len(l1)==0 or len(l1)==1:
        return True
    
    if l1[0]>=l1[1]:
        return False
        
    return checksorted2(l1[1:]) 
        