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
        pyPackages = ps:
          with ps;
          [
            # add package here
            # tkinter
          ];
      in with pkgs; {
        devShells.default = (pkgs.buildFHSUserEnv {
          name = "pipzone";
          targetPkgs = pkgs:
            (with pkgs; [ (python38.withPackages pyPackages) pipenv gmp ]);
          runScript = "bash";
        }).env;

      });
}
