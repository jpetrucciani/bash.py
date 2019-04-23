import delegator


class Bash:
    def __init__(self, *, verbose=True, interactive=False, path="bash", environ=None):
        self.interactive = interactive
        self.verbose = verbose
        self.path = path
        self.environ = environ or {}

    @property
    def about(self):
        """Returns the about page of the Bash-interpreter."""
        sub = self._exec("--version")
        if not sub.ok:
            raise RuntimeError("bash is required.")
        return str(sub.out)

    @property
    def version(self):
        """Returns the version number of the Bash-interpreter."""
        select_next = False
        for word in self.about.split():
            if select_next:
                # return 4.4.19(1)-release
                return word
            # GNU Bash, version 4.4.19(1)-release
            if word == "version":
                select_next = True

    @property
    def _flags(self):
        interactive = ["-i"] if self.interactive else []
        command = ["-c"]

        return interactive + command

    def _exec(self, *args):
        return delegator.run((self.path,) + args)


class BashScript:
    def __init__(self):
        self._contents = ""


def run(script=None, path_to_script=None):
    if not (script or path_to_script):
        raise RuntimeError


b = Bash()
print(b.version)
