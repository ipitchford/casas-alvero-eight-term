#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>

// Independent census: use s^2=14 instead of the producer's zeta basis,
// and evaluate the full G_j recurrence, including a0 and a3.
static int add[289][289], multiply[289][289], negative[289];
static int term[17][17][3][289], weight[17][289], coefficients[20], labels[20];
static std::uint64_t leaves=0, linear=0, filtered=0;
static std::array<std::uint64_t,14> hist{}, kept{};

static long long binom(int n,int k) {
    long long a=1;
    for(int j=0;j<k;j++) a=a*(n-j)/(j+1);
    return a;
}

static int pow_field(int a,int n) {
    int v=1;
    for(int i=0;i<n;i++) v=multiply[v][a];
    return v;
}

static void visit(int j,int total,int number) {
    if(j==17) {
        leaves++;
        if(total!=16) return;
        linear++; hist[number]++;
        if(labels[4]!=-1 && labels[4]==labels[16]) return;
        if(labels[5]!=-1 && labels[5]==labels[10] && labels[5]==labels[15]) return;
        filtered++; kept[number]++;
        return;
    }
    for(int choice=-1;choice<3;choice++) {
        int value=0;
        if(choice!=-1)
            for(int i=0;i<j;i++) value=add[value][term[j][i][choice][coefficients[i]]];
        coefficients[j]=negative[value];
        labels[j]=choice;
        visit(j+1,add[total][weight[j][coefficients[j]]],number+(choice!=-1));
    }
}

int main() {
    for(int x=0;x<289;x++) {
        int a=x%17,b=x/17;
        negative[x]=((17-a)%17)+17*((17-b)%17);
        for(int y=0;y<289;y++) {
            int c=y%17,d=y/17;
            add[x][y]=((a+c)%17)+17*((b+d)%17);
            multiply[x][y]=((a*c+14*b*d)%17)+17*((a*d+b*c)%17);
        }
    }
    for(int x=0;x<17;x++) if((x*x)%17==14) throw std::runtime_error("extension is reducible");
    int roots[3]={1,8+17*9,8+17*8};
    for(int e=0;e<3;e++) if(pow_field(roots[e],3)!=1) throw std::runtime_error("not cube root");
    if(roots[0]==roots[1] || roots[1]==roots[2]) throw std::runtime_error("roots not distinct");
    for(int j=4;j<=16;j++) {
        int C=(binom(20,j)/17)%17;
        for(int a=0;a<289;a++) weight[j][a]=multiply[C][a];
        for(int i=0;i<j;i++) for(int e=0;e<3;e++) {
            int factor=multiply[binom(j,i)%17][pow_field(roots[e],j-i)];
            for(int a=0;a<289;a++) term[j][i][e][a]=multiply[factor][a];
        }
    }
    coefficients[0]=1; coefficients[3]=16;
    visit(4,0,0);
    const std::array<std::uint64_t,14> expected={0,1,21,79,226,1018,4251,13291,29165,48591,58748,48406,24009,5504};
    const std::array<std::uint64_t,14> expected_filtered={0,1,21,76,210,954,3915,11830,24870,39619,45129,34622,15862,3232};
    if(leaves!=67108864 || linear!=233310 || filtered!=180341 || hist!=expected || kept!=expected_filtered)
        throw std::runtime_error("independent census disagrees");
    std::cout<<"{\"status\":\"PASS\",\"extensionBasis\":\"s^2=14\",\"recurrence\":\"full G_j\","
             <<"\"markedAssignments\":"<<leaves<<",\"afterDividedIdentity\":"<<linear
             <<",\"afterCommonRootObstructions\":"<<filtered<<",\"histogramsMatch\":true}\n";
}
