with (import <nixpkgs> {});
let
    decompyle3 = ps: (
        ps.buildPythonPackage rec {
            pname = "decompyle3";
            version = "3.9.0";
            src = fetchPypi {
                inherit pname version;
                sha256 = "sha256-IkrL+BCbTdHgJIkA4th0EKvpdtsb/MD3pSGu00L9pTA=";
            };
            doCheck = false;
            propagatedBuildInputs = [
                ps.xdis
                ps.spark_parser
            ];
        }
    );
    dep = ps: with ps;[
        pycryptodome
        (decompyle3 ps)
    ];
in
mkShell {
  buildInputs = [
    (python310Full.withPackages dep)
  ];
}