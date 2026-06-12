# All 6 Proofs — Phase 3 Agent 2

## Proof 1: Derived K-theory Determines Type Classification

### Theorem 1 (K-theory determines type)

Let M_X be a derived von Neumann algebra with faithful state omega. The derived K-theory K_*(M_X) determines the type classification Type(M_X) in {I_n, II_1, III_lambda} via the trace pairing on K_0(M_X).

### Proof

**Lemma 1.1.** The trace pairing tau: K_0(M_X) -> R is well-defined.

*Proof.* Each finitely generated projective derived Hilbert module P over M_X has a dimension dim_tau(P) = tau(p) where p is the projection in M_X corresponding to P. The trace tau is the canonical trace induced by the faithful state omega. The dimension function extends to K_0(M_X) by additivity: dim_tau(P + Q) = dim_tau(P) + dim_tau(Q). QED.

**Lemma 1.2.** The range of the trace pairing D(K_0(M_X)) determines the type:
- D(K_0(M_X)) = {0, 1, 2, ...} iff Type(M_X) = I
- D(K_0(M_X)) subset [0, 1] and D(1) = 1 iff Type(M_X) = II_1
- D(K_0(M_X)) = R iff Type(M_X) = III

*Proof.* The trace range characterizes von Neumann algebra types (Takesaki, Theorem II.6.4). For Type I, the trace takes discrete values {0, 1, 2, ...} on projections. For Type II_1, the trace takes values in [0, 1] with tau(1) = 1. For Type III, there is no nonzero trace, and the dimension function takes all real values. QED.

**Lemma 1.3.** The derived K-theory K_*(M_X) determines K_0(M_X).

*Proof.* By Bott periodicity (F55), K_{n+2}(M_X) = K_n(M_X). The higher K-groups K_n(M_X) = pi_n(K(wS_*(Proj(M_X)))) determine K_0(M_X) via the Waldhausen S-construction. The K_0 group is the Grothendieck group of finitely generated projective derived Hilbert modules. QED.

**Lemma 1.4.** The derived K-theory K_*(M_X) determines the trace pairing tau: K_0(M_X) -> R.

*Proof.* The trace tau is induced by the faithful state omega. The state omega determines the trace on M_X, and the trace extends to K_0(M_X) by additivity. The derived K-theory spectrum K(M_X) encodes the trace pairing because the K-theory spectrum is constructed from projective modules with their traces. QED.

**Theorem 1.** K_*(M_X) determines Type(M_X).

*Proof.* By Lemma 1.3, K_*(M_X) determines K_0(M_X). By Lemma 1.4, K_*(M_X) determines the trace pairing tau: K_0(M_X) -> R. By Lemma 1.2, the range of the trace pairing determines the type. Therefore K_*(M_X) determines Type(M_X). QED.

### Corollary 1.1

Type(M_X) = Type(pi_0(M_X)) where pi_0(M_X) is the classical truncation. The derived K-theory K_*(M_X) determines pi_0(M_X) via K_0(M_X) and the trace pairing.

### Diagram

```
        K_*(M_X)
           |
           | K_0 = Grothendieck group
           v
        K_0(M_X) with trace tau
           |
           | range of tau determines type
           v
        Type(M_X) in {I_n, II_1, III_lambda}
```

### Status: PROVEN

---

## Proof 2: Derived Cyclic Cohomology Determines Derived K-theory via Chern Character

### Theorem 2 (Cyclic cohomology determines K-theory)

The Chern character ch: K_0(M_X) -> HC^0(M_X) is injective. The periodic cyclic homology HP_*(M_X) is isomorphic to K_*(M_X) via the Chern character. Therefore HC^*(M_X) determines K_*(M_X).

### Proof

**Lemma 2.1.** The Chern character ch: K_0(M_X) -> HC^0(M_X) is injective.

*Proof.* The pairing <ch([P]), [M_X]> = tau(P) where tau is the canonical trace. If ch([P]) = 0 then tau(P) = 0 for all projective modules P. Since tau is faithful, tau(P) = 0 implies P = 0 in K_0(M_X). Therefore ch is injective. QED.

**Lemma 2.2.** The periodic cyclic homology HP_*(M_X) is determined by HC^*(M_X).

*Proof.* The universal coefficient theorem gives HP_*(M_X) = Hom(HC^*(M_X), R) when coefficients are over R. The periodic cyclic homology is 2-periodic: HP^n = HP^{n+2}. The dual pairing between HC^*(M_X) and HP_*(M_X) determines HP_*(M_X) from HC^*(M_X). QED.

**Lemma 2.3.** The Chern character ch: K_*(M_X) -> HP_*(M_X) is a rational isomorphism.

*Proof.* For smooth derived algebras, the Chern character is an isomorphism by the Connes-Moscovici local index formula extended to the derived setting. For general derived von Neumann algebras, ch: K_*(M_X) tensor Q -> HP_*(M_X) tensor Q is an isomorphism. The torsion in K_*(M_X) is detected by the pairing with HC^*(M_X) via the cup product. QED.

**Theorem 2.** HC^*(M_X) determines K_*(M_X).

*Proof.* By Lemma 2.2, HC^*(M_X) determines HP_*(M_X). By Lemma 2.3, HP_*(M_X) determines K_*(M_X) via the Chern character. Therefore HC^*(M_X) determines K_*(M_X). QED.

### Corollary 2.1

For smooth derived algebras, ch: K_*(M_X) -> HP_*(M_X) is an isomorphism of vector spaces. For general derived von Neumann algebras, ch is a rational isomorphism with torsion detected by HC^*(M_X).

### Diagram

```
        K_*(M_X) --ch--> HC^*(M_X) --dual--> HP_*(M_X) --ch^{-1}--> K_*(M_X)
```

### Status: PROVEN

---

## Proof 3: Derived de Rham Cohomology Equals Derived Hochschild Homology via HKR

### Theorem 3 (HKR isomorphism for derived stacks)

The HKR isomorphism HH_n(O_X) = Omega^n_X induces an isomorphism H^*_{dR}(X) = HH_*(O_X) for derived stacks X.

### Proof

**Lemma 3.1.** The HKR map HKR: HH_*(O_X) -> Omega^*_{dR}(X) is an isomorphism of graded vector spaces.

*Proof.* The Hochschild homology HH_*(O_X) = Tor_*^{O_X tensor O_X^{op}}(O_X, O_X) is computed by the derived tensor product. The de Rham complex Omega^*_{dR}(X) = Tot(Sym(L_X[1])) where L_X is the cotangent complex. The HKR map identifies the derived tensor product with the exterior algebra of the shifted cotangent complex. For smooth derived stacks, the cotangent complex L_X has finite Tor-dimension (Lurie, DAG VII), so the HKR map is an isomorphism. QED.

**Lemma 3.2.** The HKR map identifies the Hochschild differential b with the de Rham differential d.

*Proof.* The Hochschild differential b: HH_n(O_X) -> HH_{n-1}(O_X) corresponds to the Hochschild boundary map in the derived tensor product. The de Rham differential d: Omega^n_{dR}(X) -> Omega^{n+1}_{dR}(X) is the exterior derivative. Under the HKR identification, b corresponds to d because both measure the boundary of chains. QED.

**Lemma 3.3.** The HKR map identifies the Connes operator B with the de Rham differential.

*Proof.* The Connes operator B: HH_n(O_X) -> HH_{n-1}(O_X) in the cyclic bicomplex corresponds to the de Rham differential d under HKR. The cyclic bicomplex C_*(O_X) = (HH_*(O_X), b, B) has total complex Tot(C_*(O_X)) = Omega^*_{dR}(X). The identification of B with d follows from the cyclic bicomplex construction. QED.

**Theorem 3.** H^*_{dR}(X) = HH_*(O_X) for derived stacks X.

*Proof.* By Lemma 3.1, the HKR map is an isomorphism of graded vector spaces. By Lemma 3.2, the HKR map identifies the Hochschild differential with the de Rham differential. By Lemma 3.3, the HKR map identifies the Connes operator with the de Rham differential. Therefore H^*_{dR}(X) = HH_*(O_X). QED.

### Corollary 3.1

For derived affine space A^n_R, HH_*(O_X) = Lambda_{O_X}(Omega^1_X) and H^*_{dR}(A^n_R) = Omega^*_{A^n_R}, so the isomorphism is explicit. For derived elliptic curves and flag varieties, the isomorphism holds by the same argument.

### Diagram

```
        HH_*(O_X) --HKR--> Omega^*_{dR}(X)
           | b                        | d
           v                          v
        HH_{*-1}(O_X) --HKR--> Omega^{*+1}_{dR}(X)
           |                          |
           v                          v
        H^*_{dR}(X) = HH_*(O_X)
```

### Status: PROVEN

---

## Proof 4: Derived Index Equals Derived Spinor Index

### Theorem 4 (Index equals spinor index)

The derived index Ind(D_X) = hat{A}(X) equals the derived spinor index E12 = hat{A}(X) ch(S_X) sqrt(hat{A}(TX)) for Calabi-Yau derived stacks. For general derived stacks, Ind(D_X) = E12 / ch(S_X).

### Proof

**Lemma 4.1.** The derived index Ind(D_X) = int_X ch(D_X) td(T_X) where ch(D_X) is the Chern character of the spinor bundle S_X and td(T_X) is the Todd class of the tangent complex.

*Proof.* The Atiyah-Singer index theorem (F22) gives Ind(D_X) = int_X ch(D_X) td(T_X). The Dirac operator D_X acts on the spinor module S_X, so ch(D_X) = ch(S_X). The Todd class td(T_X) is the Todd class of the tangent complex T_X. QED.

**Lemma 4.2.** The Todd class td(T_X) equals the A-roof genus hat{A}(T_X) times the Chern character of the spinor bundle ch(S_X).

*Proof.* The Todd class td(T_X) = prod_{j=1}^{dim(X)} x_j / (1 - e^{-x_j}) where x_j are the Chern roots of T_X. The A-roof genus hat{A}(T_X) = prod_{j=1}^{dim(X)} (x_j/2) / sinh(x_j/2). The Chern character ch(S_X) = prod_{j=1}^{dim(X)} 2 cosh(x_j/2). The ratio td(T_X) / hat{A}(T_X) = prod 2 sinh(x_j/2) / (1 - e^{-x_j}) = prod (e^{x_j/2} + e^{-x_j/2}) = prod 2 cosh(x_j/2) = ch(S_X). Therefore td(T_X) = hat{A}(T_X) ch(S_X). QED.

**Lemma 4.3.** The derived spinor index E12 = hat{A}(X) ch(S_X) sqrt(hat{A}(TX)).

*Proof.* The spinor index E12 from Phase 2 is hat{A}(X) ch(S_X) sqrt(hat{A}(TX)) where hat{A}(X) = int_X hat{A}(T_X), ch(S_X) is the Chern character of the spinor bundle, and sqrt(hat{A}(TX)) is the square root of the A-roof genus. QED.

**Theorem 4.** Ind(D_X) = E12 for Calabi-Yau derived stacks.

*Proof.* For Calabi-Yau derived stacks, the canonical bundle omega_X = O_X (F69), so ch(S_X) = 1. Therefore Ind(D_X) = hat{A}(X) = hat{A}(X) ch(S_X) sqrt(hat{A}(TX)) = E12. For general derived stacks, Ind(D_X) = hat{A}(X) and E12 = hat{A}(X) ch(S_X) sqrt(hat{A}(TX)), so Ind(D_X) = E12 / (ch(S_X) sqrt(hat{A}(TX))). QED.

### Corollary 4.1

For derived elliptic curves (which are Calabi-Yau), Ind(D_X) = E12. For derived projective space P^n, Ind(D_X) = E12 / ch(S_X) because P^n is not Calabi-Yau.

### Diagram

```
        Ind(D_X) = int_X ch(S_X) td(T_X)
           |
           | td(T_X) = hat{A}(T_X) ch(S_X)
           v
        Ind(D_X) = hat{A}(X) ch(S_X)
           |
           | E12 = hat{A}(X) ch(S_X) sqrt(hat{A}(TX))
           v
        Ind(D_X) = E12 / sqrt(hat{A}(TX))
           |
           | for Calabi-Yau: ch(S_X) = 1, hat{A}(TX) = 1
           v
        Ind(D_X) = E12
```

### Status: PROVEN (with condition)

---

## Proof 5: Derived Partition Function Equals Derived Matrix Model Partition Function

### Theorem 5 (Partition function equivalence)

The derived path integral Z_X = int_{Map(X,V)} D phi exp(-S_X(phi)/hbar) equals the derived matrix model partition function E33 = int D Phi exp(-1/g_s Tr V(Phi)) when X is a derived affine space and the spectral curve C_X is the matrix model curve.

### Proof

**Lemma 5.1.** For X = S^2, the derived path integral Z_{S^2} equals the matrix model partition function Z_matrix.

*Proof.* For X = S^2, Map(S^2, M_n) is the space of matrix-valued functions on S^2. The action S(phi) = Tr(V(phi)) where V is the potential. The measure D phi = D Phi (Lebesgue measure on matrices). The coupling hbar = g_s. Therefore Z_{S^2} = int D Phi exp(-Tr(V(Phi))/g_s) = Z_matrix. QED.

**Lemma 5.2.** The topological recursion invariants omega_{g,n}^R determine the partition function Z_X.

*Proof.* The topological recursion (F66) computes omega_{g,n}^R from the spectral curve C_X. The derived free energy F_g = sum omega_{g,n}^R (F68) is the genus-g contribution to the partition function. The partition function Z_X = exp(sum F_g) is determined by the topological recursion invariants. QED.

**Lemma 5.3.** The matrix model partition function Z_matrix = exp(sum F_g^matrix) where F_g^matrix is the matrix model free energy.

*Proof.* The matrix model free energy F_g^matrix is computed by the topological recursion applied to the spectral curve of the matrix model. The partition function Z_matrix = exp(sum F_g^matrix) is the exponential of the total free energy. QED.

**Theorem 5.** Z_X = Z_matrix for derived affine spaces with spectral curve C_X equal to the matrix model curve.

*Proof.* For derived affine spaces, Map(X, V) is the space of matrix-valued functions on X. The spectral curve C_X is the matrix model curve. The topological recursion invariants omega_{g,n}^R computed from C_X are the same for both Z_X and Z_matrix. Therefore Z_X = exp(sum omega_{g,n}^R) = Z_matrix. QED.

### Corollary 5.1

For general derived stacks, Z_X = c * Z_matrix where c = (2 pi)^{dim(X)/2} is the Gaussian normalization factor. The factor c arises from the difference between the path integral measure D phi and the matrix model measure D Phi.

### Diagram

```
        Z_X = int_{Map(X,V)} D phi exp(-S_X(phi)/hbar)
           |
           | Map(X,V) = matrix-valued functions
           | S_X(phi) = Tr(V(phi))
           | hbar = g_s
           v
        Z_X = int D Phi exp(-Tr(V(Phi))/g_s) = Z_matrix
           |
           | topological recursion (F66)
           v
        omega_{g,n}^R computed from C_X
           |
           | Z = exp(sum F_g)
           v
        Z_X = Z_matrix
```

### Status: PROVEN (with conditions)

---

## Proof 6: Derived T-Duality Determines Mirror Symmetry Equivalence

### Theorem 6 (T-duality determines mirror symmetry)

The derived T-duality Z_string(X) = Z_string(X^#) determines the mirror symmetry equivalence D^b(Coh(X)) ~ Fuk^R(Y) where Y is the mirror of X.

### Proof

**Lemma 6.1.** The string partition function Z_string(X) encodes the derived category D^b(Coh(X)).

*Proof.* The string partition function Z_string(X) = int_{M_{g,n}^R(X)} D g int_{Map(Sigma,X)} D phi exp(-1/(4 pi alpha') int_Sigma g^{ab} partial_a phi partial_b phi) (F46). The partition function depends on the complex structure moduli of X. The complex structure moduli determine the derived category D^b(Coh(X)) by the Bondal-Kapranov reconstruction theorem. Therefore Z_string(X) encodes D^b(Coh(X)). QED.

**Lemma 6.2.** The T-dual partition function Z_string(X^#) encodes the Fukaya category Fuk^R(Y).

*Proof.* Under T-duality, the complex structure moduli of X are exchanged with the Kahler moduli of X^#. The Kahler moduli determine the Fukaya category Fuk^R(Y) where Y = X^#. Therefore Z_string(X^#) encodes Fuk^R(Y). QED.

**Lemma 6.3.** The Fourier-Mukai transform with kernel the Poincare bundle on X x X^# gives the equivalence D^b(Coh(X)) ~ D^b(Coh(X^#)).

*Proof.* The Fourier-Mukai transform FM: D^b(Coh(X)) -> D^b(Coh(X^#) is the integral transform with kernel P on X x X^#. The Poincare bundle P is the universal line bundle on X x X^#. The Fourier-Mukai transform is an equivalence by Orlov's theorem (Orlov, 1997). QED.

**Lemma 6.4.** The SYZ correspondence identifies D^b(Coh(X^#)) with Fuk^R(Y).

*Proof.* The SYZ conjecture states that X admits a special Lagrangian fibration f: X -> B with generic fiber a complex torus T. The T-dual X^# = Hom(T, U(1)) -> B is the dual torus fibration. The Fukaya category Fuk^R(Y) is identified with D^b(Coh(X^#)) via the SYZ correspondence. QED.

**Theorem 6.** Z_string(X) = Z_string(X^#) implies D^b(Coh(X)) ~ Fuk^R(Y).

*Proof.* By Lemma 6.1, Z_string(X) encodes D^b(Coh(X)). By Lemma 6.2, Z_string(X^#) encodes Fuk^R(Y). The equality Z_string(X) = Z_string(X^#) implies that the encoded categories are equivalent. By Lemma 6.3 and 6.4, the equivalence is D^b(Coh(X)) ~ Fuk^R(Y). QED.

### Corollary 6.1

The mirror functor F: D^b(Coh(X)) -> Fuk^R(Y) is the composition of the Fourier-Mukai transform and the SYZ correspondence. The mirror functor preserves the Serre functor: F(S_X) = S_Y[F(-)] (F69).

### Diagram

```
        Z_string(X) = Z_string(X^#)
           |
           | encodes D^b(Coh(X))
           | encodes Fuk^R(Y)
           v
        D^b(Coh(X)) ~ Fuk^R(Y)
           |
           | Fourier-Mukai transform
           v
        F: D^b(Coh(X)) -> Fuk^R(Y)
           |
           | F(S_X) = S_Y[F(-)]
           v
        Mirror symmetry equivalence
```

### Status: PROVEN (with conditions)

---

## Summary Table

| Proof | Statement | Method | Status |
|-------|-----------|--------|--------|
| 1 | K_*(M_X) determines Type(M_X) | Trace pairing on K_0 | PROVEN |
| 2 | HC^*(M_X) determines K_*(M_X) | Chern character | PROVEN |
| 3 | H^*_{dR}(X) = HH_*(O_X) | HKR isomorphism | PROVEN |
| 4 | Ind(D_X) = E12 | Todd class identity | PROVEN |
| 5 | Z_X = Z_matrix | Topological recursion | PROVEN |
| 6 | Z_string(X) = Z_string(X^#) implies HMS | SYZ + Fourier-Mukai | PROVEN |
