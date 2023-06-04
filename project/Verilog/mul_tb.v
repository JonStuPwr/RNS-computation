`timescale 1ns / 1ns
`include "mul_8x8_mod_13.v"

module mul_8x8_mod_13_tb;

    // polecenia do uruchomienia testbenchu:
    // iverilog -o mul_tb.vvp mul_tb.v
    // vvp mul_tb.vvp

    reg [7:0] A;
    reg [7:0] B;
    wire [3:0] S;

    // UUT - Unit Under Test
    mul_8x8_mod_13 UUT (.A(A), .B(B), .S(S));

    initial begin
        
        $dumpfile("mul_8x8_mod_13_tb.vcd");
        $dumpvars(0, mul_8x8_mod_13_tb);

        A = 8'b11111111;
        #20

        B = 8'b11111111;
        #20

        $display("Result: %d*%d mod13 = %d", A, B, S);
        $finish;

    end

endmodule
