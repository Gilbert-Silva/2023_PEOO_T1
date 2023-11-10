{ pkgs }: {
  deps = [
    pkgs.python310
    pkgs.bashInteractive
    pkgs.nodePackages.bash-language-server
    pkgs.man
  ];
}