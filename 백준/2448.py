"""
별찍기 - 11
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	11911	4006	2943	33.146%
문제
예제를 보고 별찍는 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N이 주어진다. N은 항상 3*2^k 수이다. (3, 6, 12, 24, 48, ...) (k<=10)

출력
첫째 줄부터 N번째 줄까지 별을 출력한다.

예제 입력 1
24
예제 출력 1
                       *
                      * *
                     *****
                    *     *
                   * *   * *
                  ***** *****
                 *           *
                * *         * *
               *****       *****
              *     *     *     *
             * *   * *   * *   * *
            ***** ***** ***** *****
           *                       *
          * *                     * *
         *****                   *****
        *     *                 *     *
       * *   * *               * *   * *
      ***** *****             ***** *****
     *           *           *           *
    * *         * *         * *         * *
   *****       *****       *****       *****
  *     *     *     *     *     *     *     *
 * *   * *   * *   * *   * *   * *   * *   * *
***** ***** ***** ***** ***** ***** ***** *****
"""
import math


def make_pyramid(n):
    if n == 0:
        return ['  *  ', ' * * ', '*****']
    else:
        pyramid = make_pyramid(n - 1)
        height = len(pyramid)
        margin = 3 * (2 ** (n - 1))
        for i in range(height):
            pyramid.append(pyramid[i] + ' ' + pyramid[i])
            pyramid[i] = ' ' * margin + pyramid[i] + ' ' * margin
        return pyramid


num = int(input())
pyramid = make_pyramid(int(math.log(num / 3, 2)))

for row in pyramid:
    print(row)
