module mul_8x8_mod_13 (
    input [7:0] A,
    input [7:0] B,
    output [3:0] S
);
    wire [3:0] r1 , r2 , r3 , r4;
    wire [5:0] S_temp1;
    wire [4:0] S_temp2;
    reg [3:0] S_temp;
    
    mul_4x4_mod_13 label1 (.A1(A[3:0]), .A2(A[7:4]), 
                           .B1(B[3:0]), .B2(B[7:4]), 
                           .r1(r1), .r2(r2), .r3(r3), .r4(r4));
        
    assign S_temp1 = r1 + r2 + r3 + r4;

    assign S_temp2 = S_temp1[3:0] + S_temp1[5:4] * 2'b11;

    always @(S_temp2) begin
        if (S_temp2 >= 4'b1101)
            S_temp <= S_temp2 - 4'b1101;
        else 
            S_temp <= S_temp2;
    end

    assign S = S_temp;
    
endmodule

module mul_4x4_mod_13 (
    input [3:0] A1,
    input [7:4] A2,
    input [3:0] B1,
    input [7:4] B2,
    output [3:0] r1, r2, r3, r4
);
    wire [7:0] prod_Ak_x_Bk [3:0];

    mul_4x4_bits MUL1 (.a(A1), .b(B1), .result(prod_Ak_x_Bk[0]));
    mul_4x4_bits MUL2 (.a(A1), .b(B2), .result(prod_Ak_x_Bk[1]));
    mul_4x4_bits MUL3 (.a(A2), .b(B1), .result(prod_Ak_x_Bk[2]));
    mul_4x4_bits MUL4 (.a(A2), .b(B2), .result(prod_Ak_x_Bk[3]));

    assign r1 = (prod_Ak_x_Bk[0] * 1) % 13;
    assign r2 = (prod_Ak_x_Bk[1] * 3) % 13;
    assign r3 = (prod_Ak_x_Bk[2] * 3) % 13;
    assign r4 = (prod_Ak_x_Bk[3] * 9) % 13;
    
endmodule

module mul_4x4_bits #(parameter N = 4) 
(
    input [N-1:0] a,
    input [N-1:0] b,
    output [2*N-1:0] result
);
    wire [N-1:0] part_Sout [N-1:0];
    wire [N-1:0] part_Cout [N-1:0];
    reg [2*N-1:0] product;

    generate
        genvar i;
        genvar j;
        genvar k;

        for (i=0; i<=N-1; i=i+1) begin
            multiplier MUL (.a(a[i]), 
                            .b(b[0]), 
                            .Sin(1'b0), 
                            .Cin(1'b0), 
                            .Sout(part_Sout[0][i]), 
                            .Cout(part_Cout[0][i]));
        end
        for (j=1; j<=N-1; j=j+1) begin
            for (k=0; k<=N-1; k=k+1) begin
                if (k == 0)
                    multiplier MUL (.a(a[k]), 
                                    .b(b[j]), 
                                    .Sin(part_Sout[j-1][k+1]), 
                                    .Cin(1'b0), 
                                    .Sout(part_Sout[j][k]), 
                                    .Cout(part_Cout[j][k]));
                else if (k == N-1)
                    multiplier MUL (.a(a[k]), 
                                    .b(b[j]), 
                                    .Sin(part_Cout[j-1][N-1]), 
                                    .Cin(part_Cout[j][k-1]), 
                                    .Sout(part_Sout[j][k]), 
                                    .Cout(part_Cout[j][k]));
                else
                    multiplier MUL (.a(a[k]), 
                                    .b(b[j]), 
                                    .Sin(part_Sout[j-1][k+1]), 
                                    .Cin(part_Cout[j][k-1]), 
                                    .Sout(part_Sout[j][k]), 
                                    .Cout(part_Cout[j][k]));
            end
        end
    endgenerate

    always @(*) begin
        for (integer l=0; l<=N-1; l=l+1) begin
            product[l] <= part_Sout[l][0];
        end

        for (integer l=N; l<=2*N-2; l=l+1) begin
            product[l] <= part_Sout[N-1][l-N+1];
        end

        product[2*N-1] <= part_Cout[N-1][N-1];
    end

    assign result = product;

endmodule

module multiplier (
    input a,
    input b,
    input Sin,
    input Cin,
    output Sout,
    output Cout
);
    wire a_AND_b;
    assign a_AND_b = a & b;

    full_adder FA(.x(Sin), .y(a_AND_b), .Cin(Cin), .Sout(Sout), .Cout(Cout));

endmodule

module full_adder (
    input x,
    input y,
    input Cin,
    output Sout,
    output Cout
);
    assign Sout = x ^ y ^ Cin;
    assign Cout = ((x & y) | (x & Cin) | (y & Cin));
    
endmodule
