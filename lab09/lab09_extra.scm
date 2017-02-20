;; Extra Scheme Questions ;;

; Q9
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (if (= (remainder (max a b) (min a b)) 0)
   (min a b)
   (gcd (min a b) (- (max a b) (min a b)))
   )
)


; Q10
(define (num-leaves tree)
(if (null? tree)
 0
 (if (is-leaf tree)
  1
  (if (is-leaf (left tree))
   (if (is-leaf (right tree))
    2
    (+ (num-leaves (right tree)) 1)
    )
   (if (is-leaf (right tree))
    (+ (num-leaves (left tree)) 1)
    (+ (num-leaves (right tree)) (num-leaves (left tree)))
   )
  )
)
))
(define (is-leaf tree)
 (if (null? tree)
  False
  (if (null? (left tree))
   (if (null? (right tree))
    True
    False)
   False)))

(define (count-list tree)
  (if (null? (cdr tree))
    (if (null? (car tree))
    nil
    ((lambda (num) (+ num 1))0)
    )
    (if (null? (car tree))
    (count-list (cdr tree))
    (+ (count-list (cdr tree)) 1)
   )
  )
  )


; Q11
(define (accumulate combiner start n term)
  (if (= n 0)
      start
      'YOUR-CODE-HERE
  )
)


; Binary Tree ADT
(define (make-btree entry left right)
  (cons entry (cons left right)))

(define (entry tree)
  (car tree))

(define (left tree)
  (car (cdr tree)))

(define (right tree)
  (cdr (cdr tree)))

(define test-tree
  (make-btree 2
              (make-btree 1
                          nil
                          nil)
              (make-btree 4
                          (make-btree 3
                                      nil
                                      nil)
                          nil)))

; test-tree:
;     2
;    / \
;   1   4
;      /
;     3
