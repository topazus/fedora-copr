for i <- [
  "scala3",
  "alacritty",
  "zoxide",
  "nushell",
  "flameshot",
  "bottom",
  "wezterm",
  "exa",
  "dua-cli",
  "opam",
  "bat",
  "xplr",
  "intellij-idea-ultimate",
], do:
  "https://raw.githubusercontent.com"
  |> URI.parse()
  |> URI.merge("topazus/fedora-copr/main/#{i}/#{i}.spec")
  |> to_string
  |> IO.puts
