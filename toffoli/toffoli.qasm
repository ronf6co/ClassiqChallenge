OPENQASM 2.0;
include "qelib1.inc";
qreg q_c[14];
qreg q_t[1];
qreg q_a[5];
p(pi/8) q_c[0];
p(pi/8) q_c[1];
cx q_c[0],q_c[1];
p(-pi/8) q_c[1];
cx q_c[0],q_c[1];
p(pi/8) q_c[2];
cx q_c[1],q_c[2];
p(-pi/8) q_c[2];
cx q_c[0],q_c[2];
p(pi/8) q_c[2];
cx q_c[1],q_c[2];
p(-pi/8) q_c[2];
cx q_c[0],q_c[2];
h q_a[0];
p(pi/8) q_a[0];
cx q_c[2],q_a[0];
p(-pi/8) q_a[0];
cx q_c[1],q_a[0];
p(pi/8) q_a[0];
cx q_c[2],q_a[0];
p(-pi/8) q_a[0];
cx q_c[0],q_a[0];
p(pi/8) q_a[0];
cx q_c[2],q_a[0];
p(-pi/8) q_a[0];
cx q_c[1],q_a[0];
p(pi/8) q_a[0];
cx q_c[2],q_a[0];
p(-pi/8) q_a[0];
cx q_c[0],q_a[0];
h q_a[0];
p(pi/8) q_c[3];
p(pi/8) q_c[4];
cx q_c[3],q_c[4];
p(-pi/8) q_c[4];
cx q_c[3],q_c[4];
p(pi/8) q_c[5];
cx q_c[4],q_c[5];
p(-pi/8) q_c[5];
cx q_c[3],q_c[5];
p(pi/8) q_c[5];
cx q_c[4],q_c[5];
p(-pi/8) q_c[5];
cx q_c[3],q_c[5];
h q_a[1];
p(pi/8) q_a[1];
cx q_c[5],q_a[1];
p(-pi/8) q_a[1];
cx q_c[4],q_a[1];
p(pi/8) q_a[1];
cx q_c[5],q_a[1];
p(-pi/8) q_a[1];
cx q_c[3],q_a[1];
p(pi/8) q_a[1];
cx q_c[5],q_a[1];
p(-pi/8) q_a[1];
cx q_c[4],q_a[1];
p(pi/8) q_a[1];
cx q_c[5],q_a[1];
p(-pi/8) q_a[1];
cx q_c[3],q_a[1];
h q_a[1];
p(pi/8) q_c[6];
p(pi/8) q_c[7];
cx q_c[6],q_c[7];
p(-pi/8) q_c[7];
cx q_c[6],q_c[7];
p(pi/8) q_c[8];
cx q_c[7],q_c[8];
p(-pi/8) q_c[8];
cx q_c[6],q_c[8];
p(pi/8) q_c[8];
cx q_c[7],q_c[8];
p(-pi/8) q_c[8];
cx q_c[6],q_c[8];
h q_a[2];
p(pi/8) q_a[2];
cx q_c[8],q_a[2];
p(-pi/8) q_a[2];
cx q_c[7],q_a[2];
p(pi/8) q_a[2];
cx q_c[8],q_a[2];
p(-pi/8) q_a[2];
cx q_c[6],q_a[2];
p(pi/8) q_a[2];
cx q_c[8],q_a[2];
p(-pi/8) q_a[2];
cx q_c[7],q_a[2];
p(pi/8) q_a[2];
cx q_c[8],q_a[2];
p(-pi/8) q_a[2];
cx q_c[6],q_a[2];
h q_a[2];
p(pi/8) q_a[0];
p(pi/8) q_c[9];
cx q_a[0],q_c[9];
p(-pi/8) q_c[9];
cx q_a[0],q_c[9];
p(pi/8) q_c[10];
cx q_c[9],q_c[10];
p(-pi/8) q_c[10];
cx q_a[0],q_c[10];
p(pi/8) q_c[10];
cx q_c[9],q_c[10];
p(-pi/8) q_c[10];
cx q_a[0],q_c[10];
h q_a[3];
p(pi/8) q_a[3];
cx q_c[10],q_a[3];
p(-pi/8) q_a[3];
cx q_c[9],q_a[3];
p(pi/8) q_a[3];
cx q_c[10],q_a[3];
p(-pi/8) q_a[3];
cx q_a[0],q_a[3];
p(pi/8) q_a[3];
cx q_c[10],q_a[3];
p(-pi/8) q_a[3];
cx q_c[9],q_a[3];
p(pi/8) q_a[3];
cx q_c[10],q_a[3];
p(-pi/8) q_a[3];
cx q_a[0],q_a[3];
h q_a[3];
p(pi/8) q_a[1];
p(pi/8) q_c[11];
cx q_a[1],q_c[11];
p(-pi/8) q_c[11];
cx q_a[1],q_c[11];
p(pi/8) q_c[12];
cx q_c[11],q_c[12];
p(-pi/8) q_c[12];
cx q_a[1],q_c[12];
p(pi/8) q_c[12];
cx q_c[11],q_c[12];
p(-pi/8) q_c[12];
cx q_a[1],q_c[12];
h q_a[4];
p(pi/8) q_a[4];
cx q_c[12],q_a[4];
p(-pi/8) q_a[4];
cx q_c[11],q_a[4];
p(pi/8) q_a[4];
cx q_c[12],q_a[4];
p(-pi/8) q_a[4];
cx q_a[1],q_a[4];
p(pi/8) q_a[4];
cx q_c[12],q_a[4];
p(-pi/8) q_a[4];
cx q_c[11],q_a[4];
p(pi/8) q_a[4];
cx q_c[12],q_a[4];
p(-pi/8) q_a[4];
cx q_a[1],q_a[4];
h q_a[4];
h q_t[0];
cx q_a[4],q_t[0];
tdg q_t[0];
cx q_a[3],q_t[0];
t q_t[0];
cx q_a[4],q_t[0];
tdg q_t[0];
cx q_a[3],q_t[0];
t q_t[0];
h q_t[0];
t q_a[4];
cx q_a[3],q_a[4];
t q_a[3];
tdg q_a[4];
cx q_a[3],q_a[4];
p(pi/8) q_a[1];
p(pi/8) q_c[11];
cx q_a[1],q_c[11];
p(-pi/8) q_c[11];
cx q_a[1],q_c[11];
p(pi/8) q_c[12];
cx q_c[11],q_c[12];
p(-pi/8) q_c[12];
cx q_a[1],q_c[12];
p(pi/8) q_c[12];
cx q_c[11],q_c[12];
p(-pi/8) q_c[12];
cx q_a[1],q_c[12];
h q_a[4];
p(pi/8) q_a[4];
cx q_c[12],q_a[4];
p(-pi/8) q_a[4];
cx q_c[11],q_a[4];
p(pi/8) q_a[4];
cx q_c[12],q_a[4];
p(-pi/8) q_a[4];
cx q_a[1],q_a[4];
p(pi/8) q_a[4];
cx q_c[12],q_a[4];
p(-pi/8) q_a[4];
cx q_c[11],q_a[4];
p(pi/8) q_a[4];
cx q_c[12],q_a[4];
p(-pi/8) q_a[4];
cx q_a[1],q_a[4];
h q_a[4];
p(pi/8) q_a[0];
p(pi/8) q_c[9];
cx q_a[0],q_c[9];
p(-pi/8) q_c[9];
cx q_a[0],q_c[9];
p(pi/8) q_c[10];
cx q_c[9],q_c[10];
p(-pi/8) q_c[10];
cx q_a[0],q_c[10];
p(pi/8) q_c[10];
cx q_c[9],q_c[10];
p(-pi/8) q_c[10];
cx q_a[0],q_c[10];
h q_a[3];
p(pi/8) q_a[3];
cx q_c[10],q_a[3];
p(-pi/8) q_a[3];
cx q_c[9],q_a[3];
p(pi/8) q_a[3];
cx q_c[10],q_a[3];
p(-pi/8) q_a[3];
cx q_a[0],q_a[3];
p(pi/8) q_a[3];
cx q_c[10],q_a[3];
p(-pi/8) q_a[3];
cx q_c[9],q_a[3];
p(pi/8) q_a[3];
cx q_c[10],q_a[3];
p(-pi/8) q_a[3];
cx q_a[0],q_a[3];
h q_a[3];
p(pi/8) q_c[6];
p(pi/8) q_c[7];
cx q_c[6],q_c[7];
p(-pi/8) q_c[7];
cx q_c[6],q_c[7];
p(pi/8) q_c[8];
cx q_c[7],q_c[8];
p(-pi/8) q_c[8];
cx q_c[6],q_c[8];
p(pi/8) q_c[8];
cx q_c[7],q_c[8];
p(-pi/8) q_c[8];
cx q_c[6],q_c[8];
h q_a[2];
p(pi/8) q_a[2];
cx q_c[8],q_a[2];
p(-pi/8) q_a[2];
cx q_c[7],q_a[2];
p(pi/8) q_a[2];
cx q_c[8],q_a[2];
p(-pi/8) q_a[2];
cx q_c[6],q_a[2];
p(pi/8) q_a[2];
cx q_c[8],q_a[2];
p(-pi/8) q_a[2];
cx q_c[7],q_a[2];
p(pi/8) q_a[2];
cx q_c[8],q_a[2];
p(-pi/8) q_a[2];
cx q_c[6],q_a[2];
h q_a[2];
p(pi/8) q_c[3];
p(pi/8) q_c[4];
cx q_c[3],q_c[4];
p(-pi/8) q_c[4];
cx q_c[3],q_c[4];
p(pi/8) q_c[5];
cx q_c[4],q_c[5];
p(-pi/8) q_c[5];
cx q_c[3],q_c[5];
p(pi/8) q_c[5];
cx q_c[4],q_c[5];
p(-pi/8) q_c[5];
cx q_c[3],q_c[5];
h q_a[1];
p(pi/8) q_a[1];
cx q_c[5],q_a[1];
p(-pi/8) q_a[1];
cx q_c[4],q_a[1];
p(pi/8) q_a[1];
cx q_c[5],q_a[1];
p(-pi/8) q_a[1];
cx q_c[3],q_a[1];
p(pi/8) q_a[1];
cx q_c[5],q_a[1];
p(-pi/8) q_a[1];
cx q_c[4],q_a[1];
p(pi/8) q_a[1];
cx q_c[5],q_a[1];
p(-pi/8) q_a[1];
cx q_c[3],q_a[1];
h q_a[1];
p(pi/8) q_c[0];
p(pi/8) q_c[1];
cx q_c[0],q_c[1];
p(-pi/8) q_c[1];
cx q_c[0],q_c[1];
p(pi/8) q_c[2];
cx q_c[1],q_c[2];
p(-pi/8) q_c[2];
cx q_c[0],q_c[2];
p(pi/8) q_c[2];
cx q_c[1],q_c[2];
p(-pi/8) q_c[2];
cx q_c[0],q_c[2];
h q_a[0];
p(pi/8) q_a[0];
cx q_c[2],q_a[0];
p(-pi/8) q_a[0];
cx q_c[1],q_a[0];
p(pi/8) q_a[0];
cx q_c[2],q_a[0];
p(-pi/8) q_a[0];
cx q_c[0],q_a[0];
p(pi/8) q_a[0];
cx q_c[2],q_a[0];
p(-pi/8) q_a[0];
cx q_c[1],q_a[0];
p(pi/8) q_a[0];
cx q_c[2],q_a[0];
p(-pi/8) q_a[0];
cx q_c[0],q_a[0];
h q_a[0];
