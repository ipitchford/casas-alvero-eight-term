// Independent exact enumeration; no FLINT or producer imports.
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <stdexcept>
#include <vector>
using F=std::array<int,10>;
using M=std::array<F,10>;
std::array<int,11> Q;
int md(int64_t x) { x%=17; return int(x<0?x+17:x); }
void need(bool b,const char* why) { if(!b) throw std::runtime_error(why); }
F scalar(int64_t n) { F r{};r[0]=md(n);return r; }
F add(F a,const F&b) { for(int i=0;i<10;i++)a[i]=md(a[i]+b[i]);return a; }
F scale(F a,int64_t n) { for(int&i:a)i=md(i*n);return a; }
F mul(const F&a,const F&b) {
  std::array<int64_t,19> c{};
  for(int i=0;i<10;i++)for(int j=0;j<10;j++)c[i+j]+=a[i]*b[j];
  for(int k=18;k>=10;k--) {
    int v=md(c[k]);
    for(int j=0;j<10;j++)c[k-10+j]-=v*Q[j];
  }
  F r{};for(int i=0;i<10;i++)r[i]=md(c[i]);return r;
}
F power(F a,uint64_t n) { F r=scalar(1);while(n){if(n&1)r=mul(r,a);a=mul(a,a);n>>=1;}return r; }
F eval(const std::vector<int>& f,const F&x) { F r{};for(auto i=f.rbegin();i!=f.rend();i++)r=add(mul(r,x),scalar(*i));return r; }
int64_t binom(int n,int k) { int64_t r=1;for(int i=1;i<=k;i++)r=r*(n-i+1)/i;return r; }
M matrix(const F&a) { M r{};for(int j=0;j<10;j++){F e{};e[j]=1;F v=mul(a,e);for(int i=0;i<10;i++)r[i][j]=v[i];}return r; }
F matrix_apply(const M&m,const F&a) { F r{};for(int i=0;i<10;i++){int s=0;for(int j=0;j<10;j++)s+=m[i][j]*a[j];r[i]=md(s);}return r; }

int main(int argc,char**argv) {
  need(argc==2,"input path required");std::ifstream in(argv[1]);
  int dimension,rootCount,caseCount;in>>dimension>>rootCount>>caseCount;
  need(dimension==10&&rootCount==17&&caseCount>=1&&caseCount<=240,"unexpected dimensions");
  for(int&i:Q)in>>i;need(Q[10]==1,"nonmonic field polynomial");
  uint64_t order=1;for(int i=0;i<10;i++)order*=17;
  F z{};z[1]=1;F frob=z;
  for(int i=1;i<=10;i++) {
    frob=power(frob,17);
    if(i==2||i==5) {F d=add(frob,scale(z,-1));need(mul(d,power(d,order-2))==scalar(1),"Rabin proper divisor test");}
  }
  need(frob==z,"Rabin final Frobenius test");
  std::vector<F> roots(17);for(F&r:roots)for(int&i:r)in>>i;
  std::vector<int> h(21);h[20]=1;h[17]=-1;h[2]=-3;h[1]=3;
  for(int pass=0;pass<2;pass++) {
    std::vector<int> quotient(h.size()-1);
    for(int i=int(h.size())-1;i>0;i--){quotient[i-1]=md(h[i]);h[i-1]+=quotient[i-1];}
    need(md(h[0])==0,"double-root division");h=quotient;
  }
  need(h[0]==0,"mean-root division");h.erase(h.begin());need(h.size()==18&&h.back()==1,"residue degree");
  std::vector<int> dh(17);for(int i=1;i<18;i++)dh[i-1]=md(i*h[i]);
  for(int i=0;i<17;i++) {
    need(roots[i]!=F{},"zero root retained");need(eval(h,roots[i])==F{},"root outside domain");
    need(eval(dh,roots[i])!=F{},"nonsimple domain root");
    for(int j=0;j<i;j++)need(roots[i]!=roots[j],"repeated domain root");
  }
  std::cout<<"DOMAIN_PASS 17 10\n";
  std::vector<std::array<F,17>> powers(17);
  for(int r=0;r<17;r++){powers[r][0]=scalar(1);for(int j=1;j<=16;j++)powers[r][j]=mul(powers[r][j-1],roots[r]);}
  for(int ca=0;ca<caseCount;ca++) {
    auto case_started=std::chrono::steady_clock::now();
    int m;in>>m;need(m>=3&&m<=6,"batch size");std::vector<int> active(m);for(int&j:active)in>>j;
    std::vector<int> weights(m);
    std::vector<std::array<F,17>> constant(m);
    std::vector<std::vector<std::array<M,17>>> transitions(m);
    for(int k=0;k<m;k++) {
      int j=active[k];weights[k]=md(binom(19-j,2)*(binom(20,j)/17));transitions[k].resize(k);
      for(int r=0;r<17;r++) {
        constant[k][r]=add(scale(powers[r][j],-1),scale(powers[r][j-3],binom(j,3)));
        for(int i=0;i<k;i++)transitions[k][i][r]=matrix(scale(powers[r][j-active[i]],-binom(j,active[i])));
      }
    }
    uint64_t seen=0;std::vector<std::vector<int>> survivors;std::vector<int> mark(m);std::vector<F> params(m);
    std::function<void(int,F)> visit=[&](int k,F total) {
      for(int r=0;r<17;r++) {
        mark[k]=r;F a=constant[k][r];
        for(int i=0;i<k;i++)a=add(a,matrix_apply(transitions[k][i][r],params[i]));
        params[k]=a;F t=add(total,scale(a,weights[k]));
        if(k+1<m)visit(k+1,t);else{seen++;if(t==F{})survivors.push_back(mark);}
      }
    };
    visit(0,scalar(-8037));uint64_t expected=1;for(int i=0;i<m;i++)expected*=17;need(seen==expected,"incomplete enumeration");
    std::cout<<"CASE "<<ca<<' '<<m<<' '<<seen<<' '<<survivors.size();for(int j:active)std::cout<<' '<<j;std::cout<<'\n';
    for(auto&mark:survivors){std::cout<<"SURVIVOR";for(int r:mark)std::cout<<' '<<r;std::cout<<'\n';}
    std::cout.flush();
    std::cerr<<"CASE_COMPLETE "<<ca<<" markings="<<seen<<" survivors="<<survivors.size()<<" seconds="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-case_started).count()<<std::endl;
  }
  need(bool(in),"truncated input");std::cout<<"ALL_PASS\n";
}
