"""Test qasm_parser."""
(import qasm_parser)
(import hy.pyops *)

(defn test-import []
  "Test that the package can be imported."
  (assert (isinstance qasm_parser.__name__ str)))

