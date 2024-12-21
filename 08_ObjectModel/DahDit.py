"""
Морзянка

Написать класс morse("строка"), экземпляр которого переводит арифметические
выражения в морзянку! В выражении «+» — это точка, «-» — тире, а «~» —
промежуток между буквами (бывает только между буквами и только один,
проверять не надо).
    * Параметр — строка, состоящая либо из символов, либо из слов.
    * Строка состоит из слов, если в ней есть хотя бы один пробел (в этом
      случае между словами стоит ровно один пробел)
    * Если в строке три элемента, они задают точку, точку на конце
      передаваемой буквы (традиционно обозначается другим слогом) и тире
    * Два элемента задают точку (она же точка на конце буквы) и тире
    * Если элемента четыре, четвёртый — это то, что выводится в конце
      сообщения
    * По умолчанию:
        * Если параметров нет, это слова "di", "dit" и "dah".
        * Если параметры — слова: в конце сообщения выводится ".", разделители
          при выводе: пробел между сигналами и ", " между буквами.
        * Если параметры — символы: непуст только разделитель между буквами
          (это пробел).
"""


class morse:
    def __init__(self, string='', outstr=[], letter=[]):
        self.outstr = outstr
        self.letter = letter
        if string:
            p1, *p_rest = string.split()
            if not p_rest:
                morse.sig_sep, morse.let_sep, morse.end = '', ' ', ''
                s1, s2, *s_rest = p1
                if s_rest:
                    sr1, *srr = s_rest
                    morse.dot, morse.dash, morse.dot_end = s1, sr1, s2
                    morse.end = srr[0] if srr else ''
                else:
                    morse.dot, morse.dash, morse.end = s1, s2, ''
                    morse.dot_end = morse.dot
            else:
                morse.sig_sep, morse.let_sep, morse.end = ' ', ', ', '.'
                w2, *w_rest = p_rest
                if w_rest:
                    wr1, *wrr = w_rest
                    morse.dot, morse.dash, morse.dot_end = p1, wr1, w2
                    morse.end = wrr[0] if wrr else '.'
                else:
                    morse.dot, morse.dash, morse.end = p1, w2, '.'
                    morse.dot_end = morse.dot
            if string[-1] == ' ':
                morse.end = ''

        elif not letter and not outstr:
            morse.dot, morse.dot_end, morse.dash = 'di', 'dit', 'dah'
            morse.sig_sep, morse.let_sep, morse.end = ' ', ', ', '.'

    def __pos__(self):
        return morse(outstr=self.outstr,
                     letter=[morse.dot] + self.letter) if self.letter else \
                             morse(outstr=self.outstr,
                                   letter=[morse.dot_end] + self.letter)

    def __neg__(self):
        return morse(outstr=self.outstr, letter=[morse.dash] + self.letter)

    def __invert__(self):
        return morse(outstr=[self.letter] + self.outstr, letter=[])

    def __str__(self):
        self.outstr = [self.letter] + self.outstr
        return self.let_sep.join([self.sig_sep.join(x) for x in self.outstr]) \
            + self.end


# print(-+morse())
# print(-++~+-+morse())
# print(--+~-~-++~+++-morse())
# print(--+~-~-++~+++-morse(".-"))
# print(--+~-~-++~+++-morse("..-"))
# print(--+~-~-++~+++-morse("..-|"))
# print(--+~-~-++~+++-morse("dot DOT dash"))
# print(--+~-~-++~+++-morse("ai aui oi "))
# print(--+~-~-++~+++-morse("dot dot dash ///"))
