## An introduction to Caching algorithms

### Algorithms covered
- **Least Rececently Used(*LRU*)**
Caching system where the key, value are added and when the selected memory block is filled  and there is a ```miss``` the ```Least Recently Used``` pair is removed and the new pair added to the end.

- **Most Rececently Used(*MRU*)**
In this caching system, the most recently used value is noted and in case where the memory block is filled the most recently accessed value is removed from the block

- **Segmented Least Rececently Used(*SLRU*)**
A version of LRU that used two memory segments: ```probatory``` and ```protected```. The  ```probatory``` block contains values only accessed once. If the value is accessed twice it is move to the ```protected```. The ```protected``` has finite memory and oprates under ```LRU``` where incase it is filled the least recently used value is either demoted to the ```probatory``` segment or deleted depending on the configuration.

- **Pseudo Least Rececently Used(*PLRU*)**
This system is mostly used in ```CPU caching``` systems. It is in the form of a binary tree with the nodes being marked with **bits** ```0``` and ```1```. ```0``` points to the left-node while ```1``` points to the right-node. In the case of a *miss*, the accessed path is followed according to the bits with the bits being updated either ```1``` or ```0``` depending on the current type.

- **Least Frequently Used(*LFU*)**
In a **LFU** caching system, the values are marked based on how often they are accessed and in case of a hit the elements frequency value is updated. In case of a *miss* and the memory block is filled, the element with the lowest frequency value is removed

- **Least Frequent Recently Used(*LFRU*)**
This system uses both recency and frequency of use with the value that is deleted being one with the lowest summation value of both recency and frequency.
