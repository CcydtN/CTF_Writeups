{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    # rust-overlay.url = "github:oxalica/rust-overlay";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python-packages = ps:
          with ps; [
            # opencv4
            # dlib
            # tqdm
            # tkinter
            # pycrypto
            beautifulsoup4
            requests
          ];
      in with pkgs; {
        devShells.default =
          mkShell { buildInputs = [ (python3.withPackages python-packages) ]; };
      });
}
