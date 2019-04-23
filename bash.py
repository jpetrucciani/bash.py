import delegator

DELEGATOR_MINIMUM_TIMEOUT = 60 * 60 * 60 * 8

# Monkey-patch delegator (hack):
if delegator.TIMEOUT < DELEGATOR_MINIMUM_TIMEOUT:
    delegator.TIMEOUT = DELEGATOR_MINIMUM_TIMEOUT

__all__ = ["run", "Bash"]


class BashProcess:
    def __init__(self, args, parent, blocking=True):
        # Environ inherents from parent.

        # Remember passed-in arguments.
        self.parent = parent
        self.args = args

        # Run the subprocess.
        self.sub = delegator.run(
            (self.parent.path,) + args, env=self.parent.environ, block=blocking
        )

    @property
    def output(self):
        return str(self.sub.out)

    @property
    def ok(self):
        return self.sub.ok

    def return_code(self):
        return self.sub.return_code

    def __repr__(self):
        return (
            f"<BashProcess pid={self.sub.pid!r} return_code={self.sub.return_code!r}>"
        )


class Bash:
    def __init__(self, *, verbose=True, path="bash", environ=None, interactive=False):
        self.verbose = verbose
        self.path = path
        self.interactive = interactive
        self.environ = environ.copy() if environ else {}

        ver_proc = self._exec("--version")
        if not ver_proc.ok:
            raise RuntimeError("bash is required.")
        self.about = ver_proc.output

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
        commands = ["-c"]

        return interactive + commands

    def _exec(self, *args):
        return BashProcess(parent=self, args=args)

    def command(self, script):
        return self._exec(*self._flags, script)


def run(script=None, **kwargs):
    """Runs the given bash script."""
    # Run the script.
    return Bash(**kwargs).command(script)


print(repr(run("echo $(uptime)").output))
