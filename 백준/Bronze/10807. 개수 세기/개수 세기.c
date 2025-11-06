#include <stdio.h>

int main() {
    int N;
    scanf("%d",&N);
    int a[N];
    int sum = 0;
    for(int i=0; i<N; i++){
        int b;
        scanf("%d", &b);
        a[i] = b;
    }
    int what;
    scanf("%d", &what);
    for (int i=0; i<N; i++){
        if (a[i] == what){
            sum += 1;
        }
    }
    printf("%d\n", sum);
    return 0;
}