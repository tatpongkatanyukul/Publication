# Quantum Eigenmarking

* [Paper (draft)](https://github.com/tatpongkatanyukul/Publication/blob/main/QEigenMarking/ArxivSearchEigenV2.pdf)

* [Presentation](https://github.com/tatpongkatanyukul/Publication/blob/main/QEigenMarking/EigenmarkingV4_8min.pptx) ([pdf](https://github.com/tatpongkatanyukul/Publication/blob/main/QEigenMarking/PresentationEigenmarkingV4_12Slides.pdf))

----

## Code

* [Eigenmarking](https://github.com/tatpongkatanyukul/Publication/blob/main/EigenMark_pub.ipynb)
* [Null marking](https://github.com/tatpongkatanyukul/Publication/blob/main/NullMark_pub.ipynb)
* [Subtle marking](https://github.com/tatpongkatanyukul/Publication/blob/main/SubtleMark_pub.ipynb)
* [Auxilary file](https://github.com/tatpongkatanyukul/Publication/blob/main/QLEAuxV2_pub.py): utilities
* [Compile results and visualize](https://mozart.en.kku.ac.th:8443/user/tatpong@kku.ac.th/lab/tree/Y2024/QMark/QSearchResultsV1.ipynb)

---

## Abstract

> Logic entailment is essential to reasoning, but entailment checking has the worst-case complexity of an exponential of the variable size. With recent development, quantum computing when mature may allow an effective approach for various combinatorial problems, including entailment checking.
>
> Grover algorithm uses Grover operations, i.e., selective phase inversion and amplitude amplification to address a search over unstructured data with quadratic improvement from a classical method. Its original form is intended to a single-winner scenario: exactly one match is promised. Its extension to multiple-winner cases employs probabilistic control over a number of applications of Grover operations, while a no-winner case is determined by time-out.
> 
> Our study explores various schemes of "eigenmarking" approach.
> Still relying on Grover operations, but the approach introduces additional qubits to tag the eigenstates. The tagged eigenstates are to facilitate an interpretation of the measured results and enhance identification of a no-winner case (related to no logic violation in entailment context).
> Our investigation experiments three variations of eigenmarking on a two-qubit system using an IBM Aer simulator. The results show strong distinguishability in all schemes with the best relative distinguishabilities of 19 and 53 in worst case and in average case, respectively. Our findings reveal a viable quantum mechanism to differentiate a no-winner case from other scenarios, which could play a pivot role in entailment checking and logic reasoning in general.

---

## Extra note: deriving a closed form of probability amplitudes

Grover probability amplitude
* $k_0 = \frac{1}{\sqrt{N}}$ and $\ell_0 = \frac{1}{\sqrt{N}}$

* $k_j = \frac{N-2}{N} k_{j-1} + \frac{2(N-1)}{N} \ell_{j-1}$

* $\ell_j = -\frac{2}{N} k_{j-1} + \frac{N-1}{N} \ell_{j-1}$ for $j=1,2,\ldots$

Closed form:
* $k_j = \sin( (2 j + 1) \theta )$
* $\ell_j = \frac{1}{\sqrt{N-1}} \cos( (2j + 1) \theta )$

where $\sin^2 \theta = 1/N$.

Derivation of the closed form.
1. Let's consider $j=1$,

\begin{align}
k_1 &= \frac{N-2}{N} k_0 + \frac{2(N-1)}{N} \ell_0
\end{align}

3. Let $\sin \theta \equiv \frac{1}{\sqrt{N}}$, hence

   \begin{align}
   k_1 &= \frac{N-2}{N} \sin \theta + \frac{2 \sqrt{N-1} }{N} \sqrt{N-1} \frac{1}{\sqrt{N}}
   \end{align}
   
   
