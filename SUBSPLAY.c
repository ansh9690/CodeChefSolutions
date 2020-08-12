#include <stdio.h>
#define MAX_LIMIT 100000
int main() {
	int t;
	scanf("%d\n",&t);
	while(t--){
	  int n;
	  scanf("%d\n",&n);
      char s[MAX_LIMIT]; 
      scanf("%s\n",s);
	  int ans=0,i,j,temp;
	
	  for(i=0;i<n-1;i++){
	         temp=0;
	  for(j=i+1;j<n;j++){
	         if(s[i]==s[j]){
	              temp=n-j+i;
	            if(temp>ans){
	            ans=temp;
	            }
	              break;
	                        }
	         }
	    }  
	    printf("%d\n",ans);
	     
	}
	return 0;
}