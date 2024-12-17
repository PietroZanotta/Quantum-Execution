#include <stdio.h>

int res;
int f1;
int f2;

int f11;
int f12;
int f21;
int f22;

int f111; // 8
int f112;
int f121;
int f122;
int f211;
int f212;
int f221;
int f222;

int f1111; // 16
int f1112;
int f1121;
int f1122;
int f1211;
int f1212;
int f2111;
int f2112;

int f11111; // 32
int f11112;
int f21211;
int f21212;

int main(void) {;
    int n = 5;


if (n < 1) {; // ancilla
    res= 0;
} else if (n == 1) {; // ancilla
    res= 1;
} else {;

    //fibo2(n-1)
    if(n-2<0) {// ancilla and 3 qubits (no entanglement because of the subtraction dagger, we will use again those 3 qubits when (1) appears)
        f1 = 0;
    } else if(n-2==0) {// (1), ancilla
        f1 = 1;
    } else {;
        
        //fibo1(n-2)
        if(n-3<0) {// (1), ancilla
            f11= 0;
        } else if(n-3==0) {// (1), ancilla
            f11= 1;
        } else {;

            // fibo2(n-3)
            if(n-4<0) {// (1), ancilla
                f111 = 0;
            } else if(n-4==0) {// (1), ancilla
                f111 = 1;
            } else {;

                //fibo1(n-4)
                if(n-5<0) {;// (1), ancilla
                    f1111 = 0;
                } else if(n-5==0) {;// (1), ancilla
                    f1111 = 1;
                } else {;
                    
                    //fibo1(n-5)
                    if(n-6<0) {;// (1), ancilla
                        f11111= 0;
                    } else if(n-6==0) {;// (1), ancilla
                        f11111= 1;
                    } else {;
                        
                        f11111 = 1; 
                    };

                    //fibo1(n-6)
                    if(n-7<0) {;// (1), ancilla
                        f11112= 0;
                    } else if(n-7==0) {;// (1), ancilla
                        f11112= 1;
                    } else {;
                        
                        f11112 = 1; 
                    };

                    f1111 = f11111 + f11112;
                };


                //fibo1(n-5)
                if(n-6<0) {;// (1), ancilla
                    f1112 = 0;
                } else if(n-6==0) {;// (1), ancilla
                    f1112 = 1;
                } else {;
                    
                    //fibo1(n-6)
                    if(n-7<0) {;// (1), ancilla
                        f1112= 0;
                    } else if(n-7==0) {;// (1), ancilla
                        f1112= 1;
                    } else {;
                        
                        f1112 = 1; 
                    };
                };

                f111 = f1111 + f1112;
            };

            // fibo2(n-4)
            if(n-5<0) {;// (1), ancilla
                f112 = 0;
            } else if(n-5==0) {;// (1), ancilla
                f112 = 1;
            } else {;

                //fibo1(n-5)
                if(n-6<0) {;// (1), ancilla
                    f1121 = 0;
                } else if(n-6==0) {;// (1), ancilla
                    f1121 = 1;
                } else {;
                    
                    //fibo1(n-6)
                    if(n-7<0) {;// (1), ancilla
                        f1121= 0;
                    } else if(n-7==0) {;// (1), ancilla
                        f1121= 1;
                    } else {;
                        
                        f1121 = 1; 
                    };
                };

                //fibo1(n-6)
                if(n-7<0) {;// (1), ancilla
                    f1122 = 0;
                } else if(n-7==0) {;// (1), ancilla
                    f1122 = 1;
                } else {;
                };

                f112 = f1121 + f1122;
            };

            f11= f111 + f112;
        };
        
        //fibo1(n-3)
        if(n-4<0) {;// (1), ancilla
            f12= 0;
        } else if(n-4==0) {;// (1), ancilla
            f12= 1;
        } else {;

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


            fibo2(n-4)
            if(n-5<0) {;// (1), ancilla
                f121 = 0;
            } else if(n-5==0) {;// (1), ancilla
                f121 = 1;
            } else {;

                fibo1(n-5) 
                if(n-6<0) {;// (1), ancilla
                    f1211 = 0;
                } else if(n-6==0) {;// (1), ancilla
                    f1211 = 1;
                } else {;
                    
                    fibo1(n-6) 
                    if(n-7<0) {;// (1), ancilla
                        f1211= 0;
                    } else if(n-7==0) {;// (1), ancilla
                        f1211= 1;
                    } else {;
                        
                        f1211 = 1; 
                    };

                };

                fibo1(n-6)
                if(n-7<0) {;// (1), ancilla
                    f1212 = 0;
                } else if(n-7==0) {;// (1), ancilla
                    f1212 = 1;
                } else {;
                };

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


                f121 = f1211 + f1212;
            };


            fibo2(n-5) 
            if(n-6<0) {;// (1), ancilla
                f122 = 0;
            } else if(n-6==0) {;// (1), ancilla
                f122 = 1;
            } else {;

                fibo1(n-6) 
                if(n-7<0) {;// (1), ancilla
                    f122 = 0;
                } else if(n-7==0) {;// (1), ancilla
                    f122 = 1;
                } else {;
                    
                };
            };

            f12= f121 + f122;
        };

        f1 = f11 + f12;
    };

    fibo2(n-2)
    if(n-3<0) {;// (1), ancilla
        f2 = 0;
    } else if(n-3==0) {;// (1), ancilla
        f2 = 1;
    } else {;
        
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


        fibo1(n-3)
        if(n-4<0) {;// (1), ancilla
            f21= 0;
        } else if(n-4==0) {;// (1), ancilla
            f21= 1;
        } else {;

            fibo2(n-4)
            if(n-5<0) {;// (1), ancilla
                f211 = 0;
            } else if(n-5==0) {;// (1), ancilla
                f211 = 1;
            } else {;

                fibo1(n-5)
                if(n-6<0) {;// (1), ancilla
                    f2111 = 0;
                } else if(n-6==0) {;// (1), ancilla
                    f2111 = 1;
                } else {;
                    
                    fibo1(n-6)
                    if(n-7<0) {;// (1), ancilla
                        f2111= 0;
                    } else if(n-7==0) {;// (1), ancilla
                        f2111= 1;
                    } else {;
                        
                        f2111 = 1; 
                    };
                };

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

                fibo1(n-6)
                if(n-7<0) {;// (1), ancilla
                    f2112 = 0;
                } else if(n-7==0) {;// (1), ancilla
                    f2112 = 1;
                } else {;
                };

                f211 = f2111 + f2112;
            };

            fibo2(n-5)
            if(n-6<0) {;// (1), ancilla
                f212 = 0;
            } else if(n-6==0) {;// (1), ancilla
                f212 = 1;
            } else {;

                fibo1(n-6)
                if(n-7<0) {;// (1), ancilla
                    f212 = 0;
                } else if(n-7==0) {;// (1), ancilla
                    f212 = 1;
                } else {;
                };
            };

            f21 = f211 + f212;
        };
        
        fibo1(n-4)
        if(n-5<0) {;// (1), ancilla
            f22= 0;
        } else if(n-5==0) {;// (1), ancilla
            f22= 1;
        } else {;


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

            fibo2(n-5)
            if(n-6<0) {;// (1), ancilla
                f221 = 0;
            } else if(n-6==0) {;// (1), ancilla
                f221 = 1;
            } else {;

                //fibo1(n-6) 
                if(n-7<0) {;// (1), ancilla
                    f221 = 0;
                } else if(n-7==0) {;// (1), ancilla
                    f221 = 1;
                } else {;
                    
                };

            };

            // fibo2(n-6) 
            if(n-7<0) {;// (1), ancilla
                f222 = 0;
            } else if(n-7==0) {;// (1), ancilla
                f222 = 1;
            } else {;
            };

            f22= f221 + f222;
        };


        f2 = f21 + f22;
    };

    res= f1 + f2;
};

    printf("%d\n", res);
    return 0;
};