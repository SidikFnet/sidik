#!/system/bin/sh

password="prima"
while [ "$masukkan" != "$password" ]
do
read -p "masukkan password anda :" masukkan
done
echo "selamat password yang anda masukkan benar"
sleep 1
pilih="y"
while [ $pilih="y" ];
do
echo " (1)scan UII"
read -p "Masukkan nomer 1 :" pilih;
if [ $pilih="1" ];
sleep 1
then
echo "Installing Software..."
cd $home
git clone https://github.com/SidikFnet/sidik/
cd sidik
python rului.py
fi
done