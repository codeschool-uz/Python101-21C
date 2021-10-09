# bool16

Ikkita **a** va **b** butun sonlari berilgan, quydagi iborani tekshiring "Ikkala a va b sonlaridan kamida bittasi toq son".

**Input**:*a va b. (Butun son)*.\
**Output**: *bool*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|5   8          |True             |
|4   8         |False             |

# bool17

**a** butun son berilgan, quydagi iborani tekshiring "a butun soni ikki xonali son".

**Input**:*a. (Butun son)*.\
**Output**: *bool*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|28             |True             |
|4              |False            |

# bool18

**a** ikki xonali butun son berilgan, quydagi iborani tekshiring "a ikki xonali butun sonning xamma raqamlari bir xil".

**Input**:*a. (Butun son)*.\
**Output**: *bool*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|22             |True             |
|87             |False            |

# bool19

**a** besh xonali butun son berilgan, quydagi iborani tekshiring "a besh xonali sonning barcha xona birligidagi raqamlari o’sish tartibida joylashgan".

**Input**:*a. (Butun son)*.\
**Output**: *bool*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|54321          |True             |
|79682          |False            |

# bool20

**a** besh xonali butun son berilgan, quydagi iborani tekshiring "a besh xonali sonning barcha xona birligidagi raqamlari kamayish tartibida joylashgan".

**Input**:*a. (Butun son)*.\
**Output**: *bool*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|12345          |True             |
|46829          |False            |

# If statements

# if01

**a** butun son berilgan, agar ushbu son musbat son bulsa 1 ga oshirilsin, aks xolda o’zgarishsiz qolsin.

**Input**:*a. (int)*.\
**Output**: *Natijani chiqaring(int)*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|6              |7                |
|-5             |-5               |

# if02

**a**butun son berilgan, agar ushbu son musbat son bulsa 1 ga oshirilsin , aks xolda 2 ga kamaytirilsin.

**Input**:*a. (int)*.\
**Output**: *Natijani chiqaring(int)*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|9              |10               |
|-6             |-8               |

# if03

**a**, **b**, **c** uchta butun son berilgan, shu sonlar ichida nechta musbat son borligi aniqlansin.

**Input**:*a, b, c. (int)*.\
**Output**: *Natijani chiqaring(int)*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|1   3   8      |3                |
|-1  9  -3      |1                |

# if04

**a**, **b**, **c** butun sonlar berilgan, shu sonlarning qaysi biri kichikligini aniqlang.

**Input**:*a, b, c. (int)*.\
**Output**: *Natijani chiqaring(int)*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|5  8  1        |1                |
|4  -9  23      |-9               |

# if05

**a**, **b**, **c** butun sonlar berilgan, shu sonlarning o’rtachasi (ya’ni katta va kichik son o’rtasidagi) sonni aniqlang.

**Input**:*a, b, c. (int)*.\
**Output**: *Natijani chiqaring(int)*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|50  89  1      |50               |
|40  -20  23    |23               |

# if06

**X** va **Y** dekart koordinata o`qlarida yotmaydigan (x; y) nuqta berilgan. Shu nuqta joylashgan koordinata choragini aniqlang.

**Input**:*x, y. (int)*.\
**Output**: *Natijani chiqaring*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|7  3           |I - chorak       |
|-5  6          |II - chorak      |
|-8  -1         |III - chorak     |
|5  -12         |IV - chorak      |

# if07

**x** haqiqiy son berilgan. Quyidagi funksiyani hisoblang..
<img src="https://latex.codecogs.com/gif.latex?f(x)=\left\{\begin{matrix}2*\sin(x), agar\rightarrow x>0;\\ x-6,agar\rightarrow x\leq 0;\end{matrix}\right." />.

**Input**:*x. (float)*.\
**Output**: *Natijani chiqaring*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|0.5            |0.958851077208406 |
|-5.0           |-11.0            |

