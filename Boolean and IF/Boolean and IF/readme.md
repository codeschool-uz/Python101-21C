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

**a**, **b**, **c**kesmalar berilgan. Uchburchak yasash mumkinligiga tekshiring.
Agar mumkin bolsa “Yes” aks holda “No” javob qaytarsin.\

Uchburchak yasash sharti: Ixtiyoriy 2 ta tomonning yig`indisi qolgan 3-tomondan katta bo`lishi kerak.

**Input**:*a, b, c. (int)*.\
**Output**: *Yes yoki No (string)*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|3  4  5        |Yes              |
|7  4  2        |No               |

# if08

Sizga harorat selsiyda berilgan quyidagi harorat holatiga muvofiq habarni ko`rsating:

Temp<0: "Freezing"
Temp 1-10: "Very Cold"
Temp 11-20: "Cold"
Temp 21-30: "Normal"
Temp 31-40: "Hot"
Temp >40: "Very Hot"

**Input**:*Temp. (int)*.\
**Output**: *Natijani chiqaring*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|28             |Normal           |
|-4             |Freezing         |
|58             |Very Hot         |

# if09

**a** butun son berilgan. Ushbu sonni quyidagi shartlarga tekshiring:

"musbat toq son" 
"musbat juft son"
"manfiy toq son"
"manfiy juft son"
"son 0 ga teng"

Kiritilgan sonning qanday sonligini yozuv bilan chiqaring.

**Input**:*a. (int)*.\
**Output**: *Natijani chiqaring*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|10             |musbat juft son  |
|-7             |manfiy toq son   |
|0              |son 0 ga teng    |

# if10

**a** butun son berilgan. Ushbu sonni quyidagi shartlarga tekshiring:

"Ikki xonali toq son" 
"Ikki xonali juft son"
"Uch xonali toq son”"
"Uch xonali juft son"

Kiritilgan sonning qanday sonligini yozuv bilan chiqaring.

**Input**:*a. (int) a butun sonni faqat shu oraliqda oling 1<a<999*.\
**Output**: *Natijani chiqaring*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|30             |Ikki xonali juft son |
|101            |Uch xonali toq son|

# if11

Do`konchi biron kishiga daftar berish yoki bermaslik kerakligini aniqlash uchun dastur yozmoqchi. Do`konchi daftarga yetarli puli borlarga va tanaffusda bo`lganlarga Daftar beradi.

Shaxsning pulini va tanaffus vaqtini hisobga olgan holda unga daftar berish kerakmi yo`qmi aniqlaydigan dastur tuzing.
*Tanaffusda bo`lgandagi qiymati 1 ga tanaffusda bo`lmasa 0 ga teng. Daftarning narhi: 20 (UZS).*


**Input**:*price, on_break. (butun,0 yoki 1)*.\
**Output**: *Natijani chiqaring(bool)*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|17  1          |False            |
|30  1          |True             |

# if12

n  ikki xonali son berilgan uning raqamlar joyini almashtirganda hosil bo`lgan son n sonidan kichik yoki teng bo`lsa True aks holda False qaytaradigan dastur tuzing.

**Input**:*n, (int)*.\
**Output**: *Natijani chiqaring*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|99             |True             |
|27             |False            |

# if13

n  butun son nechi xonali son ekanligini topadigan dastur tuzing.

**Input**:*n. ( Butun son. 0 < n <100000)*.\
**Output**: *Natijani chiqaring*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|45             |2                |
|8481           |4                |

# if14

n  butun sonining raqamlari yig`indisini toping.

**Input**:*n. ( Butun son. 0 < n <10000 )*.\
**Output**: *Natijani chiqaring*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|345            |12               |
|45             |9                |

# if15

n  butun sonining toq raqamlari yig`indisini toping.

**Input**:*n. ( Butun son. 0 < n <10000 )*.\
**Output**: *Natijani chiqaring*.

|   **Input**   |   **Output**    |
|---------------|-----------------|
|8481           |1                |
|345            |8                |