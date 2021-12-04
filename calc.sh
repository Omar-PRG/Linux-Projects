echo "Saisir le premier numero"
read n1
echo "Saisir le deuxieme"
read n2
echo "1.addition"
echo "2.substraction"
echo "3.multiplication"
echo "4.division"
echo "enter your choice"
read ch
case $ch in 
1)
echo "scale = 2; $n1 + $n2" | bc
;; 
2)
echo "scale = 2; $n1 - $n2" | bc
;; 
3)
echo "scale = 2; $n1 *  $n2" | bc
;;
4)
echo "scale = 2; $n1 / $n2" | bc
;; 

*)echo "invalid choice";;
esac

