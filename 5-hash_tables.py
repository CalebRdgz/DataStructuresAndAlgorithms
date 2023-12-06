#hash tables explained:
#built in hash table - (dictionary) = "key": value pair
#{"nails": 1000}: "nails" is the key, 1000 is the value
#use hash function/method to perform a hash on the key to get an address which is 
#returned from the hash function
#a hash function is ONE WAY meaning once we get the address, we cant take it away
#hash is deterministic, every time we put nails in, we get 2 every time
#even though python has hash tables already, were creating our own
#ex.) Hardware Store
#"key": value pair
#{"nails": 1000} <-- run this through a hash method, perform a hash on the key, 
#and get an address(index) where we store that key value pair
#a hash is ONE WAY - pass "nails" through the hash and get 2, cant go backwards
#hash is DETERMINISTIC - every time we put "nails" through the hash, we will always get 2

#COLLISIONS
