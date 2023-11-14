import filetype
import os
import re

prefix = "hw4"

def test_setup_netid():
    """
    To pass this test case, you need to add your (and your partner's) Net ID to
    the `netids` file in the root directory of your repository. 
    Delete the Net ID placeholder lines
    """

    with open('netids', 'r') as inf:
        lines = inf.readlines()

    assert len(lines) <= 2, "At most two netids"

    dummy_netids = ["NETID_GOES_HERE", "ONE_NETID_PER_LINE"]
    for line in lines:
        netid = str(line.strip())
        assert netid not in dummy_netids, "Add your NetID"
        assert netid.lower() == netid, "Lowercase NetID, please"
        assert re.search(r"^[a-z]{3}[0-9]{3,4}$", netid) is not None, "Your NetID looks like xyz0123"

    files = os.listdir(".")

    # Please include a PDF output of your notebook
    pdf_fn = f"{prefix}.pdf"
    assert pdf_fn in files, f"Please create {pdf_fn}"
    guess = filetype.guess(pdf_fn)
    msg = f"Is {pdf_fn} actually a pdf?"
    assert guess is not None, msg
    assert guess.mime == 'application/pdf', msg

    ipynb_fn = f"{prefix}.ipynb"
    assert ipynb_fn in files, f"Please save your work in {ipynb_fn}"


def test_setup_other_ipynbs():
    
    ipynb_fn = f"{prefix}.ipynb"
    for (root, dirs, files) in os.walk("."):
        if root.startswith("./.ipynb_checkpoints"):
            continue
        if root.startswith("./lectures"):
            continue

        for fn in files:
            msg = " ".join([
                f"We'll only grade {ipynb_fn}, not {root}/{fn}.",
                f"As long as the work you want graded is in {ipynb_fn}"
                " in your root directory, you can ignore this error."
            ])
            if fn.endswith("ipynb"):
                assert root == "." and fn == f"{prefix}.ipynb", msg


def test_setup_late_days():
    '''
    If you want to use late days, list the integer number of days to use.
    '''
    with open('LATE_DAYS', 'r') as inf:
        lines = inf.readlines()
        try:
            n_days = int(lines[0].strip())
        except Exception as e:
            assert e is None, "Couldn't read n_days as integer"
