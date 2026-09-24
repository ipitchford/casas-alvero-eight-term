#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>

// F_17[zeta]/(zeta^2+zeta+1), element a+17*b represents a+b*zeta.
// The complete enumeration concerns residue assignments only, not lifts.
static int plus17[289][289], minus17[289][289], rotate17[3][289];
static int transform[17][17][3][289], weighted[17][289], base[17][3];
static int a[20], witness[20];
static std::uint64_t total=0, pass=0, pass_no_collisions=0;
static std::uint64_t strata[17][17];
static std::array<std::uint64_t,14> histogram{}, filtered{};
static std::array<std::array<int,13>,14> samples{};
static std::array<bool,14> has_sample{};

static long long choose(int n,int k) {
    if(k<0 || k>n) return 0;
    long long r=1;
    for(int i=1;i<=k;i++) r=r*(n-i+1)/i;
    return r;
}

static int scalar(int c,int x) {
    c=(c%17+17)%17;
    return (c*(x%17)%17)+17*(c*(x/17)%17);
}

static void enumerate(int j,int sum,int units) {
    if(j==17) {
        ++total;
        if(sum!=16) return;
        ++pass;
        ++histogram[units];
        bool pair=witness[4]>=0 && witness[4]==witness[16];
        bool triple=witness[5]>=0 && witness[5]==witness[10] && witness[5]==witness[15];
        if(pair || triple) return;
        ++pass_no_collisions;
        int J=0,L=0;
        for(int i=4;i<=16;i++) { if(witness[i]>=0) J=i; if(a[i]!=0) L=i; }
        if(L<4 || L>J) throw std::runtime_error("invalid stratum");
        ++strata[J][L];
        ++filtered[units];
        if(!has_sample[units]) {
            has_sample[units]=true;
            for(int i=4;i<=16;i++) samples[units][i-4]=witness[i];
        }
        return;
    }
    witness[j]=-1;
    a[j]=0;
    enumerate(j+1,sum,units);
    for(int e=0;e<3;e++) {
        int x=base[j][e];
        for(int i=4;i<j;i++) x=minus17[x][transform[j][i][e][a[i]]];
        a[j]=x;
        witness[j]=e;
        enumerate(j+1,plus17[sum][weighted[j][x]],units+1);
    }
}

int main() {
    for(int x=0;x<289;x++) for(int y=0;y<289;y++) {
        plus17[x][y]=((x%17+y%17)%17)+17*((x/17+y/17)%17);
        minus17[x][y]=((x%17-y%17+17)%17)+17*((x/17-y/17+17)%17);
    }
    for(int x=0;x<289;x++) {
        int u=x%17,v=x/17;
        rotate17[0][x]=x;
        rotate17[1][x]=((17-v)%17)+17*((u-v+17)%17);
        rotate17[2][x]=((v-u+17)%17)+17*((17-u)%17);
    }
    // All rotation entries are initialized before this exhaustive check.
    for(int x=0;x<289;x++)
        if(rotate17[1][rotate17[2][x]]!=x || rotate17[2][rotate17[1][x]]!=x)
            throw std::runtime_error("rotation inverse check failed");
    for(int j=4;j<=16;j++) {
        long long C=choose(20,j);
        if(C%17) throw std::runtime_error("coefficient not divisible by17");
        for(int x=0;x<289;x++) weighted[j][x]=scalar(C/17,x);
        for(int e=0;e<3;e++) {
            base[j][e]=rotate17[(e*j)%3][(choose(j,3)-1)%17];
            for(int i=4;i<j;i++) for(int x=0;x<289;x++)
                transform[j][i][e][x]=scalar(choose(j,i),rotate17[(e*(j-i))%3][x]);
        }
    }
    a[0]=1; a[3]=16;
    enumerate(4,0,0);
    if(total!=(std::uint64_t(1)<<26)) throw std::runtime_error("incomplete enumeration");
    if(histogram[0] || histogram[1]!=1 || filtered[1]!=1)
        throw std::runtime_error("single-unit classification differs");
    std::cerr<<"{\n  \"status\": \"PASS\",\n  \"strata\": [";
    bool first_stratum=true;
    std::uint64_t nondegenerate=0,degenerate=0;
    for(int J=4;J<=16;J++) for(int L=4;L<=J;L++) if(strata[J][L]) {
        if(J==L) nondegenerate+=strata[J][L]; else degenerate+=strata[J][L];
        std::cerr<<(first_stratum?"\n":",\n")<<"    {\"lastUnitDegree\":"<<J<<",\"lastUnitCoefficientDegree\":"<<L<<",\"count\":"<<strata[J][L]<<"}";
        first_stratum=false;
    }
    std::cerr<<"\n  ],\n  \"nondegenerateAssignments\": "<<nondegenerate<<",\n  \"degenerateAssignments\": "<<degenerate<<",\n  \"totalFilteredAssignments\": "<<pass_no_collisions<<"\n}\n";
    std::cout<<"{\n  \"status\": \"PASS\",\n  \"totalMarkedAssignments\": "<<total
             <<",\n  \"afterDividedIdentity\": "<<pass
             <<",\n  \"afterUnitRootCollisionObstructions\": "<<pass_no_collisions<<",\n";
    std::cout<<"  \"histogramByNumberOfUnitWitnesses\": [";
    for(int i=0;i<14;i++) std::cout<<(i?", ":"")<<histogram[i];
    std::cout<<"],\n  \"filteredHistogram\": [";
    for(int i=0;i<14;i++) std::cout<<(i?", ":"")<<filtered[i];
    std::cout<<"],\n  \"sampleUnitRootExponentsByWitnessCount\": {";
    bool first=true;
    for(int i=0;i<14;i++) if(has_sample[i]) {
        std::cout<<(first?"\n":",\n")<<"    \""<<i<<"\": ["; first=false;
        for(int j=0;j<13;j++) std::cout<<(j?", ":"")<<samples[i][j];
        std::cout<<"]";
    }
    std::cout<<"\n  },\n  \"scope\": \"Complete finite residue enumeration only. No characteristic-zero lift or whole row8 exclusion is asserted.\"\n}\n";
}
