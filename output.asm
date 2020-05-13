.model small

.data
x0 db 0
x1 db 1
x2 db 0
i, db ?
n db 10
in dw ?
out dw ?

.code
mov ah, 01h
int 21h
mov in, al
mov ax,  in

mov n , ax
mov ax,  0
mov i , ax
l0:
mov ax,  i 
mov bx,  n
cmp ax, bx
jge l1
mov ax,  x0 
mov bx,  x1

add ax, bx
mov x2 , ax
mov ax,  x1

mov x0 , ax
mov ax,  x2

mov x1 , ax
mov ax,  x2

mov out , ax
mov dl, out
mov ah, 02h
int 21h
inc  i
jmp l0
l1:

mov ah, 4ch
int 21h

end
