#include <stdio.h>

extern int __VERIFIER_nondet_int();
extern void abort(void);
extern void __assert_fail(const char *, const char *, unsigned int, const char *) __attribute__ ((__nothrow__ , __leaf__)) __attribute__ ((__noreturn__));
void reach_error() { __assert_fail("0", "fibo_2calls_5-1.c", 4, "reach_error"); };



int res;
int f1;
int f2;

int f11;
int f12;
int f21;
int f22;

int f111;
int f112;
int f121;
int f122;
int f211;
int f212;
int f221;
int f222;

int f1111;
int f1112;
int f1121;
int f1122;
int f1211;
int f1212;
int f1221;
int f1222;
int f2111;
int f2112;
int f2121;
int f2122;
int f2211;
int f2212;
int f2221;
int f2222;

int f11111;
int f11112;
int f11121;
int f11122;
int f11211;
int f11212;
int f11221;
int f11222;
int f12111;
int f12112;
int f12121;
int f12122;
int f12211;
int f12212;
int f12221;
int f12222;
int f21111;
int f21112;
int f21121;
int f21122;
int f21211;
int f21212;
int f21221;
int f21222;
int f22111;
int f22112;
int f22121;
int f22122;
int f22211;
int f22212;
int f22221;
int f22222;




int main(void) {;
    int n = 7;
    
if (n < 1) {;
    res= 0;
} else if (n == 1) {;
    res= 1;
} else {;

    //fibo2(n-1)
    if (n-1 < 1) {;
        f1 = 0;
    } else if (n-1 == 1) {;
        f1 = 1;
    } else {;
        
        //fibo1(n-2)
        if (n-2 < 1) {;
            f11= 0;
        } else if (n-2 == 1) {;
            f11= 1;
        } else {;

            // fibo2(n-3)
            if (n-3 < 1) {;
                f111 = 0;
            } else if (n-3 == 1) {;
                f111 = 1;
            } else {;

                //fibo1(n-4)
                if (n-4 < 1) {;
                    f1111 = 0;
                } else if (n-4 == 1) {;
                    f1111 = 1;
                } else {;
                    
                    //fibo1(n-5)
                    if (n-5 < 1) {;
                        f11111= 0;
                    } else if (n-5 == 1) {;
                        f11111= 1;
                    } else {;
                        
                        f11111 = 1; 
                    };

                    //fibo1(n-6)
                    if (n-6 < 1) {;
                        f11112= 0;
                    } else if (n-6 == 1) {;
                        f11112= 1;
                    } else {;
                        
                        f11112 = 1; 
                    };

                    f1111 = f11111 + f11112;
                };


                //fibo1(n-5)
                if (n-5 < 1) {;
                    f1112 = 0;
                } else if (n-5 == 1) {;
                    f1112 = 1;
                } else {;
                    
                    //fibo1(n-6)
                    if (n-6 < 1) {;
                        f11121= 0;
                    } else if (n-6 == 1) {;
                        f11121= 1;
                    } else {;
                        
                        f11121 = 1; 
                    };

                    //fibo1(n-7)
                    if (n-7 < 1) {;
                        f11122= 0;
                    } else if (n-7 == 1) {;
                        f11122= 1;
                    } else {;
                        
                        f11122 = 0; 
                    };

                    f1112 = f11121 + f11122;
                };

                f111 = f1111 + f1112;
            };

            // fibo2(n-4)
            if (n-4 < 1) {;
                f112 = 0;
            } else if (n-4 == 1) {;
                f112 = 1;
            } else {;

                //fibo1(n-5)
                if (n-5 < 1) {;
                    f1121 = 0;
                } else if (n-5 == 1) {;
                    f1121 = 1;
                } else {;
                    
                    //fibo1(n-6)
                    if (n-6 < 1) {;
                        f11211= 0;
                    } else if (n-6 == 1) {;
                        f11211= 1;
                    } else {;
                        
                        f11211 = 1; 
                    };

                    //fibo1(n-7)
                    if (n-7 < 1) {;
                        f11212= 0;
                    } else if (n-7 == 1) {;
                        f11212= 1;
                    } else {;
                        
                        f11212 = 0; 
                    };

                    f1121 = f11211 + f11212;
                };


                //fibo1(n-6)
                if (n-6 < 1) {;
                    f1122 = 0;
                } else if (n-6 == 1) {;
                    f1122 = 1;
                } else {;
                    
                    //fibo1(n-7)
                    if (n-7 < 1) {;
                        f11221= 0;
                    } else if (n-7 == 1) {;
                        f11221= 1;
                    } else {;
                        
                        f11221 = 0; 
                    };

                    //fibo1(n-8)
                    if (n-8 < 1) {;
                        f11222= 0;
                    } else if (n-8 == 1) {;
                        f11222= 1;
                    } else {;
                        
                        f11222 = 0; 
                    };

                    f1122 = f11221 + f11222;
                };

                f112 = f1121 + f1122;
            };

            f11= f111 + f112;
        };
        
        //fibo1(n-3)
        if (n-3 < 1) {;
            f12= 0;
        } else if (n-3 == 1) {;
            f12= 1;
        } else {;

            // fibo2(n-4)
            if (n-4 < 1) {;
                f121 = 0;
            } else if (n-4 == 1) {;
                f121 = 1;
            } else {;

                //fibo1(n-5) 
                if (n-5 < 1) {;
                    f1211 = 0;
                } else if (n-5 == 1) {;
                    f1211 = 1;
                } else {;
                    
                    //fibo1(n-6) 
                    if (n-6 < 1) {;
                        f12111= 0;
                    } else if (n-6 == 1) {;
                        f12111= 1;
                    } else {;
                        
                        f12111 = 1; 
                    };

                    //fibo1(n-7) 
                    if (n-7 < 1) {;
                        f12112= 0;
                    } else if (n-7 == 1) {;
                        f12112= 1;
                    } else {;
                        
                        f12112 = 0; 
                    };

                    f1211 = f12111 + f12112;
                };


                //fibo1(n-6)
                if (n-6 < 1) {;
                    f1212 = 0;
                } else if (n-6 == 1) {;
                    f1212 = 1;
                } else {;
                    
                    //fibo1(n-7) 
                    if (n-7 < 1) {;
                        f12121= 0;
                    } else if (n-7 == 1) {;
                        f12121= 1;
                    } else {;
                        
                        f12121 = 0; 
                    };

                    //fibo1(n-8) 
                    if (n-8 < 1) {;
                        f12122= 0;
                    } else if (n-8 == 1) {;
                        f12122= 1;
                    } else {;
                        
                        f12122 = 0; 
                    };

                    f1212 = f12121 + f12122;
                };

                f121 = f1211 + f1212;
            };

            // fibo2(n-5) 
            if (n-5 < 1) {;
                f122 = 0;
            } else if (n-5 == 1) {;
                f122 = 1;
            } else {;

                //fibo1(n-6) 
                if (n-6 < 1) {;
                    f1221 = 0;
                } else if (n-6 == 1) {;
                    f1221 = 1;
                } else {;
                    
                    //fibo1(n-7)
                    if (n-7 < 1) {;
                        f12211= 0;
                    } else if (n-7 == 1) {;
                        f12211= 1;
                    } else {;
                        
                        f12211 = 0; 
                    };

                    //fibo1(n-8)
                    if (n-8 < 1) {;
                        f12212= 0;
                    } else if (n-8 == 1) {;
                        f12212= 1;
                    } else {;
                        
                        f12212 = 0; 
                    };

                    f1221 = f12211 + f12212;
                };


                //fibo1(n-7) 
                if (n-7 < 1) {;
                    f1222 = 0;
                } else if (n-7 == 1) {;
                    f1222 = 1;
                } else {;
                    
                    //fibo1(n-8) 
                    if (n-8 < 1) {;
                        f12221= 0;
                    } else if (n-8 == 1) {;
                        f12221= 1;
                    } else {;
                        
                        f12221 = 0; 
                    };

                    //fibo1(n-9)
                    if (n-9 < 1) {;
                        f12222= 0;
                    } else if (n-9 == 1) {;
                        f12222= 1;
                    } else {;
                        
                        f12222 = 0; 
                    };

                    f1222 = f12221 + f12222;
                };

                f122 = f1221 + f1222;
            };

            f12= f121 + f122;
        };

        f1 = f11 + f12;
    };

    //fibo2(n-2)
    if (n-2 < 1) {;
        f2 = 0;
    } else if (n-2 == 1) {;
        f2 = 1;
    } else {;
        
        //fibo1(n-3)
        if (n-3 < 1) {;
            f21= 0;
        } else if (n-3 == 1) {;
            f21= 1;
        } else {;

            // fibo2(n-4)
            if (n-4 < 1) {;
                f211 = 0;
            } else if (n-4 == 1) {;
                f211 = 1;
            } else {;

                //fibo1(n-5)
                if (n-5 < 1) {;
                    f2111 = 0;
                } else if (n-5 == 1) {;
                    f2111 = 1;
                } else {;
                    
                    //fibo1(n-6)
                    if (n-6 < 1) {;
                        f21111= 0;
                    } else if (n-6 == 1) {;
                        f21111= 1;
                    } else {;
                        
                        f21111 = 1; 
                    };

                    //fibo1(n-7)
                    if (n-7 < 1) {;
                        f21112= 0;
                    } else if (n-7 == 1) {;
                        f21112= 1;
                    } else {;
                        
                        f21112 = 0; 
                    };

                    f2111 = f21111 + f21112;
                };


                //fibo1(n-6)
                if (n-6 < 1) {;
                    f2112 = 0;
                } else if (n-6 == 1) {;
                    f2112 = 1;
                } else {;
                    
                    //fibo1(n-7)
                    if (n-7 < 1) {;
                        f21121= 0;
                    } else if (n-7 == 1) {;
                        f21121= 1;
                    } else {;
                        
                        f21121 = 0; 
                    };

                    //fibo1(n-8)
                    if (n-8 < 1) {;
                        f21122= 0;
                    } else if (n-8 == 1) {;
                        f21122= 1;
                    } else {;
                        
                        f21122 = 0; 
                    };

                    f2112 = f21121 + f21122;
                };

                f211 = f2111 + f2112;
            };

            // fibo2(n-5)
            if (n-5 < 1) {;
                f212 = 0;
            } else if (n-5 == 1) {;
                f212 = 1;
            } else {;

                //fibo1(n-6)
                if (n-6 < 1) {;
                    f2121 = 0;
                } else if (n-6 == 1) {;
                    f2121 = 1;
                } else {;
                    
                    //fibo1(n-7)
                    if (n-7 < 1) {;
                        f21211= 0;
                    } else if (n-7 == 1) {;
                        f21211= 1;
                    } else {;
                        
                        f21211 = 1; 
                    };

                    //fibo1(n-8)
                    if (n-8 < 1) {;
                        f21212= 0;
                    } else if (n-8 == 1) {;
                        f21212= 1;
                    } else {;
                        
                        f21212 = 0; 
                    };

                    f2121 = f21211 + f21212;
                };


                //fibo1(n-7)
                if (n-7 < 1) {;
                    f2122 = 0;
                } else if (n-7 == 1) {;
                    f2122 = 1;
                } else {;
                    
                    //fibo1(n-8)
                    if (n-8 < 1) {;
                        f21221= 0;
                    } else if (n-8 == 1) {;
                        f21221= 1;
                    } else {;
                        
                        f21221 = 0; 
                    };

                    //fibo1(n-9)
                    if (n-9 < 1) {;
                        f21222= 0;
                    } else if (n-9 == 1) {;
                        f21222= 1;
                    } else {;
                        
                        f21222 = 0; 
                    };

                    f2122 = f21221 + f21222;
                };

                f212 = f2121 + f2122;
            };

            f21= f211 + f212;
        };
        
        //fibo1(n-4)
        if (n-4 < 1) {;
            f22= 0;
        } else if (n-4 == 1) {;
            f22= 1;
        } else {;

            // fibo2(n-5)
            if (n-5 < 1) {;
                f221 = 0;
            } else if (n-5 == 1) {;
                f221 = 1;
            } else {;

                //fibo1(n-6) 
                if (n-6 < 1) {;
                    f2211 = 0;
                } else if (n-6 == 1) {;
                    f2211 = 1;
                } else {;
                    
                    //fibo1(n-7) 
                    if (n-7 < 1) {;
                        f22111= 0;
                    } else if (n-7 == 1) {;
                        f22111= 1;
                    } else {;
                        
                        f22111 = 0; 
                    };

                    //fibo1(n-8) 
                    if (n-8 < 1) {;
                        f22112= 0;
                    } else if (n-8 == 1) {;
                        f22112= 1;
                    } else {;
                        
                        f22112 = 0; 
                    };

                    f2211 = f22111 + f22112;
                };


                //fibo1(n-7)
                if (n-7 < 1) {;
                    f2212 = 0;
                } else if (n-7 == 1) {;
                    f2212 = 1;
                } else {;
                    
                    //fibo1(n-8) 
                    if (n-8 < 1) {;
                        f22121= 0;
                    } else if (n-8 == 1) {;
                        f22121= 1;
                    } else {;
                        
                        f22121 = 0; 
                    };

                    //fibo1(n-9) 
                    if (n-9 < 1) {;
                        f22122= 0;
                    } else if (n-9 == 1) {;
                        f22122= 1;
                    } else {;
                        
                        f22122 = 0; 
                    };

                    f2212 = f22121 + f22122;
                };

                f221 = f2211 + f2212;
            };

            // fibo2(n-6) 
            if (n-6 < 1) {;
                f222 = 0;
            } else if (n-6 == 1) {;
                f222 = 1;
            } else {;

                //fibo1(n-7) 
                if (n-7 < 1) {;
                    f2221 = 0;
                } else if (n-7 == 1) {;
                    f2221 = 1;
                } else {;
                    
                    //fibo1(n-8)
                    if (n-8 < 1) {;
                        f22211= 0;
                    } else if (n-8 == 1) {;
                        f22211= 1;
                    } else {;
                        
                        f22211 = 0; 
                    };

                    //fibo1(n-9)
                    if (n-9 < 1) {;
                        f22212= 0;
                    } else if (n-9 == 1) {;
                        f22212= 1;
                    } else {;
                        
                        f22212 = 0; 
                    };

                    f2221 = f22211 + f22212;
                };


                //fibo1(n-8) 
                if (n-8 < 1) {;
                    f2222 = 0;
                } else if (n-8 == 1) {;
                    f2222 = 0;
                } else {;
                    
                    //fibo1(n-9) 
                    if (n-9 < 1) {;
                        f22221= 0;
                    } else if (n-9 == 1) {;
                        f22221= 1;
                    } else {;
                        
                        f22221 = 0; 
                    };

                    //fibo1(n-10)
                    if (n-10 < 1) {;
                        f22222= 0;
                    } else if (n-10 == 1) {;
                        f22222= 1;
                    } else {;
                        
                        f22222 = 0; 
                    };

                    f2222 = f22221 + f22222;
                };

                f222 = f2221 + f2222;
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
