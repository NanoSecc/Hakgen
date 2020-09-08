echo "\n"
echo -------------------
echo Script Made By Nano
echo --------------------
echo
echo "\n"
echo Created Invite
echo "\n"
curl -XPOST https://www.hackthebox.eu/api/invite/generate -s | cut -c-70 | cut -c30-69 | base64 -d
echo "\n"
echo " Invite Code ^"
