spec start;
prog: test;
test: number@num -> output(num);

#Functions

output(num){
    MCI [
        num:w(8,0):(0.8)
    ]
}
